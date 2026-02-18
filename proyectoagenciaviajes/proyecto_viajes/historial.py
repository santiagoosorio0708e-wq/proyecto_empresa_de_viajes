# historial.py
# Módulo para mostrar el historial de un usuario:
# - Viajes reservados
# - Reservas realizadas
# - Préstamos de carros
# - Puntos ganados/perdidos
# - Beneficios obtenidos por proveedores (hoteles, etc.)
#
# Importante:
# - No usa clases, solo funciones y diccionarios.
# - Está pensado para trabajar con estructuras sencillas
#   que ya deberías tener en otros módulos (usuarios, reservas, carros, puntos, proveedores).

import time


def filtrar_reservas_por_nombre_usuario(lista_de_reservas, nombre_usuario):
    """
    Devuelve una lista con las reservas cuyo nombre_cliente
    coincide exactamente con el nombre del usuario.
    """
    reservas_usuario = []

    for reserva in lista_de_reservas:
        if "nombre_cliente" in reserva and reserva["nombre_cliente"] == nombre_usuario:
            reservas_usuario.append(reserva)

    return reservas_usuario


def filtrar_prestamos_por_id_usuario(lista_de_prestamos, id_usuario):
    """
    Devuelve una lista con los préstamos de carro
    que pertenecen al id_usuario indicado.
    """
    prestamos_usuario = []

    for prestamo in lista_de_prestamos:
        if "id_usuario" in prestamo and prestamo["id_usuario"] == id_usuario:
            prestamos_usuario.append(prestamo)

    return prestamos_usuario


def filtrar_movimientos_puntos_por_id_usuario(lista_movimientos_puntos, id_usuario):
    """
    Devuelve una lista con los movimientos de puntos
    que pertenecen al id_usuario indicado.
    Cada movimiento debería tener:
    - id_usuario
    - tipo ("ganado" o "gastado")
    - puntos
    - descripcion
    """
    movimientos_usuario = []

    if lista_movimientos_puntos is None:
        return movimientos_usuario

    for mov in lista_movimientos_puntos:
        if "id_usuario" in mov and mov["id_usuario"] == id_usuario:
            movimientos_usuario.append(mov)

    return movimientos_usuario


def filtrar_beneficios_proveedores_por_id_usuario(lista_beneficios_proveedores, id_usuario):
    """
    Devuelve una lista con los beneficios de proveedores
    (descuentos por hoteles, etc.) que pertenecen al id_usuario.
    Cada beneficio debería tener:
    - id_usuario
    - proveedor (nombre del hotel/empresa)
    - porcentaje_descuento
    - descripcion
    """
    beneficios_usuario = []

    if lista_beneficios_proveedores is None:
        return beneficios_usuario

    for ben in lista_beneficios_proveedores:
        if "id_usuario" in ben and ben["id_usuario"] == id_usuario:
            beneficios_usuario.append(ben)

    return beneficios_usuario


def calcular_resumen_puntos(movimientos_puntos):
    """
    Calcula puntos ganados, puntos gastados y saldo final
    a partir de una lista de movimientos de puntos.
    """
    puntos_ganados = 0
    puntos_gastados = 0

    for mov in movimientos_puntos:
        tipo = mov.get("tipo", "").lower()
        cantidad = mov.get("puntos", 0)

        if tipo == "ganado":
            puntos_ganados += cantidad
        elif tipo == "gastado":
            puntos_gastados += cantidad

    saldo = puntos_ganados - puntos_gastados
    return puntos_ganados, puntos_gastados, saldo


def mostrar_historial_usuario(
    usuario,
    lista_de_viajes,
    lista_de_reservas,
    lista_de_prestamos_carro,
    lista_movimientos_puntos,
    lista_beneficios_proveedores
):
    """
    Muestra en pantalla el historial completo de un usuario:
    - Datos básicos del usuario
    - Reservas de viajes
    - Préstamos de carros
    - Resumen de puntos (ganados, gastados y saldo)
    - Beneficios obtenidos por proveedores (descuentos)
    """
    if usuario is None:
        print("No se ha proporcionado un usuario válido.")
        time.sleep(1)
        return

    id_usuario = usuario.get("id_usuario", "N/A")
    nombre_usuario = usuario.get("nombre", "SIN NOMBRE")

    print("\n========== HISTORIAL DEL USUARIO ==========")
    print("ID de usuario:", id_usuario)
    print("Nombre:", nombre_usuario)
    print("Email:", usuario.get("email", "SIN EMAIL"))
    print("Teléfono:", usuario.get("telefono", "SIN TELÉFONO"))
    print("===========================================")
    time.sleep(1)

    # 1. Reservas de viajes (filtradas por nombre del usuario)
    reservas_usuario = filtrar_reservas_por_nombre_usuario(lista_de_reservas, nombre_usuario)

    print("\n--- Reservas de viajes del usuario ---")
    if len(reservas_usuario) == 0:
        print("Este usuario no tiene reservas registradas por nombre.")
    else:
        for reserva in reservas_usuario:
            id_reserva = reserva.get("id_reserva", "N/A")
            id_viaje = reserva.get("id_viaje", "N/A")
            plazas = reserva.get("plazas", 0)

            # Buscamos datos básicos del viaje
            destino = "DESCONOCIDO"
            fecha_inicio = "?"
            fecha_fin = "?"
            for viaje in lista_de_viajes:
                if viaje.get("id_viaje") == id_viaje:
                    destino = viaje.get("destino", "DESCONOCIDO")
                    fecha_inicio = viaje.get("fecha_inicio", "?")
                    fecha_fin = viaje.get("fecha_fin", "?")
                    break

            print(
                "Reserva ID:", id_reserva,
                "| Viaje ID:", id_viaje,
                "| Destino:", destino,
                "| Fechas:", fecha_inicio, "-", fecha_fin,
                "| Plazas:", plazas
            )

    time.sleep(1)

    # 2. Préstamos de carros
    prestamos_usuario = filtrar_prestamos_por_id_usuario(lista_de_prestamos_carro, id_usuario)

    print("\n--- Préstamos de carros del usuario ---")
    if len(prestamos_usuario) == 0:
        print("Este usuario no tiene préstamos de carros registrados.")
    else:
        for prestamo in prestamos_usuario:
            print(
                "Préstamo ID:", prestamo.get("id_prestamo", "N/A"),
                "| Viaje ID:", prestamo.get("id_viaje", "N/A"),
                "| Marca:", prestamo.get("marca", "DESCONOCIDA"),
                "| Días previstos:", prestamo.get("dias_previstos", 0),
                "| Días reales:", prestamo.get("dias_reales", 0),
                "| Costo final carro:", prestamo.get("costo_final_carro", 0.0),
                "| Hotel reservado:", prestamo.get("hotel_reservado", "SIN HOTEL"),
                "| Total a pagar (carro + hotel):", prestamo.get("total_pagar", 0.0)
            )

    time.sleep(1)

    # 3. Puntos del usuario
    movimientos_usuario = filtrar_movimientos_puntos_por_id_usuario(
        lista_movimientos_puntos,
        id_usuario
    )

    print("\n--- Puntos del usuario ---")
    if len(movimientos_usuario) == 0:
        print("Este usuario no tiene movimientos de puntos registrados.")
    else:
        puntos_ganados, puntos_gastados, saldo = calcular_resumen_puntos(movimientos_usuario)
        print("Puntos ganados:", puntos_ganados)
        print("Puntos gastados:", puntos_gastados)
        print("Saldo total de puntos:", saldo)
        print("\nDetalle de movimientos de puntos:")
        for mov in movimientos_usuario:
            print(
                "Fecha:", mov.get("fecha", "SIN FECHA"),
                "| Tipo:", mov.get("tipo", "SIN TIPO"),
                "| Puntos:", mov.get("puntos", 0),
                "| Descripción:", mov.get("descripcion", "")
            )

    time.sleep(1)

    # 4. Beneficios de proveedores
    beneficios_usuario = filtrar_beneficios_proveedores_por_id_usuario(
        lista_beneficios_proveedores,
        id_usuario
    )

    print("\n--- Beneficios obtenidos por proveedores ---")
    if len(beneficios_usuario) == 0:
        print("Este usuario no tiene beneficios registrados por proveedores.")
    else:
        for ben in beneficios_usuario:
            print(
                "Proveedor:", ben.get("proveedor", "SIN PROVEEDOR"),
                "| Descuento aplicado:", ben.get("porcentaje_descuento", 0), "%",
                "| Descripción:", ben.get("descripcion", "")
            )

    print("\n========== FIN DEL HISTORIAL ==========")
    time.sleep(1)