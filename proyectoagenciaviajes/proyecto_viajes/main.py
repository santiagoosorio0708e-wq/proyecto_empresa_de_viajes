
from datetime import date
import time
import datos
import servicios
import hospedaje
import moneda
import usuarios
import carros
import puntos
import proveedores
import historial

ARCHIVO_VIAJES = "viajes.txt"
ARCHIVO_RESERVAS = "reservas.txt"


def mostrar_menu():
    """
    Imprime en pantalla las opciones del menú principal.
    """
    print("\n========== Panel de Administración de Viajes ==========")
    print("1. Ver viajes y reservas agrupadas por viaje")
    print("2. Añadir nuevo viaje")
    print("3. Añadir nueva reserva manual")
    print("4. Ver detalle de destino (viaje + hotel + restaurante)")
    print("5. Limpiar viajes ya finalizados")
    print("6. Generar texto para redes sociales de un viaje")
    print("7. Comparar moneda natal con moneda del país de visita")
    print("8. Registrar nuevo usuario")
    print("9. Renta de carro (ligada a usuario, viaje y hotel)")
    print("10. Puntos y recompensas de usuario")
    print("11. Beneficios con proveedores (descuentos por hotel)")
    print("12. Ver historial completo de usuario")
    print("13. Salir")
    print("=======================================================")
    print("=======================================================")


def mostrar_viajes_agrupados(lista_de_viajes, lista_de_reservas):
    """
    Muestra por pantalla los viajes y sus reservas agrupadas.
    """
    agrupado = servicios.agrupar_reservas_por_viaje(lista_de_viajes, lista_de_reservas)

    if len(agrupado) == 0:
        print("No hay viajes cargados.")
        return

    for id_viaje in agrupado:
        info = agrupado[id_viaje]
        viaje = info["viaje"]
        reservas = info["reservas"]
        total_plazas = info["total_plazas"]

        print("\n---------------------------------")
        print("ID del viaje:", viaje["id_viaje"])
        print("Destino:", viaje["destino"])
        print("Fechas:", viaje["fecha_inicio"], "hasta", viaje["fecha_fin"])
        print("Precio por persona:", viaje["precio"], "EUR")
        print("Total de plazas reservadas:", total_plazas)

        if len(reservas) == 0:
            print("No hay reservas para este viaje.")
            time.sleep(1)
        else:
            print("Reservas:")
            for reserva in reservas:
                print(
                    "  - ID Reserva:",
                    reserva["id_reserva"],
                    "| Cliente:",
                    reserva["nombre_cliente"],
                    "| Plazas:",
                    reserva["plazas"]
                )


def opcion_ver_detalle_destino(lista_de_viajes):
    """
    Permite elegir un viaje por su ID y muestra:
    - Datos del viaje (destino, fechas, precio)
    - Datos del hotel asociado al destino
    - Datos del restaurante asociado al destino
    """
    print("\n--- Ver detalle de destino (viaje + hotel + restaurante) ---")

    if len(lista_de_viajes) == 0:
        print("No hay viajes disponibles.")
        time.sleep(1)
        return

    print("Viajes disponibles:")
    for viaje in lista_de_viajes:
        print(
            "ID:", viaje["id_viaje"],
            "| Destino:", viaje["destino"],
            "| Fechas:", viaje["fecha_inicio"], "-", viaje["fecha_fin"],
            "| Precio por persona:", viaje["precio"], "EUR"
        )

    id_viaje = input("Introduce el ID del viaje para ver el detalle: ").strip()

    viaje_encontrado = servicios.buscar_viaje_por_id(lista_de_viajes, id_viaje)
    if viaje_encontrado is None:
        print("No existe un viaje con ese ID.")
        time.sleep(1)
        return

    destino = viaje_encontrado["destino"]

    info_hospedaje = hospedaje.obtener_hospedaje_por_destino(destino)

    print("\n===== Detalle del destino =====")
    print("ID del viaje:", viaje_encontrado["id_viaje"])
    print("Destino:", destino)
    print("Fechas:", viaje_encontrado["fecha_inicio"], "hasta", viaje_encontrado["fecha_fin"])
    print("Precio del viaje por persona:", viaje_encontrado["precio"], "EUR")
    time.sleep(1)

    if info_hospedaje is None:
        print("\nNo hay información de hotel y restaurante guardada para este destino.")
        time.sleep(1)
    else:
        print("\n--- Información de hospedaje y restaurante ---")
        print("Hotel recomendado:", info_hospedaje["hotel"])
        print("Precio por noche en el hotel:", info_hospedaje["precio_noche"], "EUR")
        print("Restaurante recomendado:", info_hospedaje["restaurante"])
        print("Precio aproximado del plato del día:", info_hospedaje["precio_plato_dia"], "EUR")
        time.sleep(1)


def opcion_agregar_viaje(lista_de_viajes):
    """
    Pide al usuario los datos de un nuevo viaje y lo agrega
    a la lista de viajes (memoria) y al archivo de viajes.
    """
    print("\n--- Añadir nuevo viaje ---")

    destino = input("Destino del viaje: ").strip()
    fecha_inicio = input("Fecha de inicio (dd/mm/aaaa): ").strip()
    fecha_fin = input("Fecha de fin (dd/mm/aaaa): ").strip()
    precio_texto = input("Precio por persona (ej: 450.0): ").strip()

    try:
        precio = float(precio_texto)
    except ValueError:
        print("El precio debe ser un número. Operación cancelada.")
        time.sleep(1)
        return

    if precio <= 0:
        print("El precio debe ser mayor que cero. Operación cancelada.")
        time.sleep(1)
        return

    fecha_inicio_obj = servicios.convertir_texto_a_fecha(fecha_inicio)
    fecha_fin_obj = servicios.convertir_texto_a_fecha(fecha_fin)

    if fecha_inicio_obj is None or fecha_fin_obj is None:
        print("Alguna de las fechas no tiene el formato correcto (dd/mm/aaaa).")
        time.sleep(1)
        return

    if fecha_fin_obj < fecha_inicio_obj:
        print("La fecha de fin no puede ser anterior a la fecha de inicio.")
        time.sleep(1)
        return

    nuevo_viaje = servicios.generar_nuevo_viaje_en_memoria(
        lista_de_viajes,
        destino,
        fecha_inicio,
        fecha_fin,
        precio
    )

    datos.agregar_viaje_en_archivo(ARCHIVO_VIAJES, nuevo_viaje)

    print("Viaje creado con éxito. ID del viaje:", nuevo_viaje["id_viaje"])
    time.sleep(1)


def opcion_agregar_reserva(lista_de_viajes, lista_de_reservas):
    """
    Pide al usuario los datos de una nueva reserva y la agrega
    a la lista de reservas y al archivo de reservas.
    """
    print("\n--- Añadir nueva reserva ---")

    if len(lista_de_viajes) == 0:
        print("No hay viajes disponibles. No se puede crear una reserva.")
        time.sleep(1)
        return

    print("Viajes disponibles:")
    for viaje in lista_de_viajes:
        print(
            "ID:", viaje["id_viaje"],
            "| Destino:", viaje["destino"],
            "| Fechas:", viaje["fecha_inicio"], "-", viaje["fecha_fin"]
        )

    id_viaje = input("Introduce el ID del viaje para la reserva: ").strip()

    viaje_encontrado = servicios.buscar_viaje_por_id(lista_de_viajes, id_viaje)
    if viaje_encontrado is None:
        print("No existe un viaje con ese ID. Reserva cancelada.")
        time.sleep(1)
        return

    nombre_cliente = input("Nombre del cliente: ").strip()

    plazas_texto = input("Número de plazas a reservar: ").strip()
    try:
        plazas = int(plazas_texto)
    except ValueError:
        print("El número de plazas debe ser un número entero. Reserva cancelada.")
        time.sleep(1)
        return

    if plazas <= 0:
        print("El número de plazas debe ser mayor que cero. Reserva cancelada.")
        time.sleep(1)
        return

    nueva_reserva = servicios.generar_nueva_reserva_en_memoria(
        lista_de_reservas,
        id_viaje,
        nombre_cliente,
        plazas
    )

    datos.agregar_reserva_en_archivo(ARCHIVO_RESERVAS, nueva_reserva)

    print("Reserva creada con éxito. ID de la reserva:", nueva_reserva["id_reserva"])


def opcion_limpiar_viajes(lista_de_viajes, lista_de_reservas):
    """
    Limpia los viajes que ya finalizaron y sus reservas asociadas.
    Actualiza las listas y guarda los cambios en los archivos.
    """
    print("\n--- Limpiar viajes ya finalizados ---")

    if len(lista_de_viajes) == 0:
        print("No hay viajes para limpiar.")
        time.sleep(1)
        return lista_de_viajes, lista_de_reservas

    fecha_hoy = date.today()

    nuevos_viajes, nuevas_reservas = servicios.limpiar_viajes_pasados(
        lista_de_viajes,
        lista_de_reservas,
        fecha_hoy
    )

    cantidad_antes = len(lista_de_viajes)
    cantidad_despues = len(nuevos_viajes)
    eliminados = cantidad_antes - cantidad_despues

    datos.guardar_viajes(ARCHIVO_VIAJES, nuevos_viajes)
    datos.guardar_reservas(ARCHIVO_RESERVAS, nuevas_reservas)

    print("Se han eliminado", eliminados, "viaje(s) finalizado(s).")
    time.sleep(1)
    return nuevos_viajes, nuevas_reservas


def opcion_generar_texto_redes(lista_de_viajes, lista_de_reservas):
    """
    Permite elegir un viaje y muestra en pantalla un texto
    preparado para publicar en redes sociales.
    """
    print("\n--- Generar texto para redes sociales ---")

    if len(lista_de_viajes) == 0:
        print("No hay viajes disponibles.")
        time.sleep(1)
        return

    for viaje in lista_de_viajes:
        print(
            "ID:", viaje["id_viaje"],
            "| Destino:", viaje["destino"],
            "| Fechas:", viaje["fecha_inicio"], "-", viaje["fecha_fin"]
        )

    id_viaje = input("Introduce el ID del viaje para generar el texto: ").strip()

    viaje_encontrado = servicios.buscar_viaje_por_id(lista_de_viajes, id_viaje)
    if viaje_encontrado is None:
        print("No existe un viaje con ese ID.")
        time.sleep(1)
        return

    total_reservas = servicios.contar_plazas_reservadas_para_viaje(
        lista_de_reservas,
        id_viaje
    )

    mensaje = servicios.generar_texto_redes_para_viaje(
        viaje_encontrado,
        total_reservas
    )

    print("\nTexto sugerido para redes sociales:\n")
    print(mensaje)
    time.sleep(1)
    print("\n(Lo puedes copiar y pegar en tus redes.)")


def opcion_comparar_moneda():
    """
    Pide al usuario su moneda natal, la moneda del país de visita
    y una cantidad, y muestra la conversión.
    """
    print("\n--- Comparación de moneda natal con moneda del país de visita ---")
    print("Ejemplos de códigos de moneda: EUR, USD, MXN, ARS, CLP, COP, BRL, GBP, JPY, CNY, CAD, AUD, PEN, BOB, ZAR, MAD, EGP, TRY")

    codigo_origen = input("Introduce el código de tu moneda natal (ej: EUR, MXN): ")
    codigo_destino = input("Introduce el código de la moneda del país que visitas: ")
    cantidad_texto = input("Introduce la cantidad en tu moneda natal: ")

    try:
        cantidad = float(cantidad_texto)
    except ValueError:
        print("La cantidad debe ser un número. Operación cancelada.")
        time.sleep(1)
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero. Operación cancelada.")
        time.sleep(1)
        return

    resultado = moneda.convertir_moneda(codigo_origen, codigo_destino, cantidad)

    if resultado is None:
        print("Alguna de las monedas no está registrada en el sistema.")
        print("Revisa los códigos de moneda y vuelve a intentarlo.")
        time.sleep(1)
    else:
        origen = codigo_origen.strip().upper()
        destino = codigo_destino.strip().upper()
        print(f"\n{cantidad:.2f} {origen} equivalen aproximadamente a {resultado:.2f} {destino}.")
        time.sleep(1)


def opcion_registrar_usuario(lista_de_usuarios):
    """
    Registra un nuevo usuario y lo guarda en memoria y en archivo.
    """
    print("\n--- Registrar nuevo usuario ---")

    nombre = input("Nombre completo del usuario: ").strip()
    email = input("Correo electrónico: ").strip()
    telefono = input("Teléfono de contacto: ").strip()

    nuevo_usuario = usuarios.generar_nuevo_usuario_en_memoria(
        lista_de_usuarios,
        nombre,
        email,
        telefono
    )

    usuarios.guardar_usuario_en_archivo(nuevo_usuario)

    print("Usuario registrado con éxito. ID del usuario:", nuevo_usuario["id_usuario"])
    time.sleep(1)


def opcion_rentar_carro(lista_de_usuarios, lista_de_viajes, lista_de_prestamos):
    """
    Gestiona la renta de un carro para un usuario y viaje específicos,
    incluyendo el cálculo del costo del hotel según el destino.
    """
    print("\n--- Renta de carro (usuario + viaje + hotel) ---")

    if len(lista_de_usuarios) == 0:
        print("No hay usuarios registrados. Registra un usuario primero.")
        time.sleep(1)
        return

    if len(lista_de_viajes) == 0:
        print("No hay viajes disponibles. Crea un viaje primero.")
        time.sleep(1)
        return

    print("\nUsuarios registrados:")
    for usuario in lista_de_usuarios:
        print(
            "ID:", usuario["id_usuario"],
            "| Nombre:", usuario["nombre"],
            "| Email:", usuario["email"]
        )

    id_usuario = input("Introduce el ID del usuario que rentará el carro: ").strip()
    usuario_encontrado = usuarios.buscar_usuario_por_id(lista_de_usuarios, id_usuario)
    if usuario_encontrado is None:
        print("No existe un usuario con ese ID.")
        time.sleep(1)
        return

    print("\nViajes disponibles:")
    for viaje in lista_de_viajes:
        print(
            "ID:", viaje["id_viaje"],
            "| Destino:", viaje["destino"],
            "| Fechas:", viaje["fecha_inicio"], "-", viaje["fecha_fin"]
        )

    id_viaje = input("Introduce el ID del viaje asociado al préstamo del carro: ").strip()
    viaje_encontrado = servicios.buscar_viaje_por_id(lista_de_viajes, id_viaje)
    if viaje_encontrado is None:
        print("No existe un viaje con ese ID.")
        time.sleep(1)
        return

    destino = viaje_encontrado["destino"]
    info_hospedaje = hospedaje.obtener_hospedaje_por_destino(destino)

    if info_hospedaje is None:
        print("No hay información de hotel para este destino. Aun así se calculará solo el costo del carro.")
        time.sleep(1)
    else:
        print("\nHotel sugerido para este destino:", info_hospedaje["hotel"])
        print("Precio por noche:", info_hospedaje["precio_noche"], "EUR")

    print("\nMarcas de carro disponibles (ignora mayúsculas/minúsculas):")
    for marca in carros.MARCAS_CARRO:
        print("- ", marca)

    nombre_marca = input("Escribe la marca de carro que quieres rentar: ")

    precio_base = carros.obtener_precio_base_marca(nombre_marca)
    if precio_base is None:
        print("La marca ingresada no está registrada. Operación cancelada.")
        time.sleep(1)
        return

    dias_previstos_texto = input("Número de días de préstamo acordados: ")
    dias_reales_texto = input("Número de días reales de uso del carro: ")

    try:
        dias_previstos = int(dias_previstos_texto)
        dias_reales = int(dias_reales_texto)
    except ValueError:
        print("Los días deben ser números enteros. Operación cancelada.")
        time.sleep(1)
        return

    if dias_previstos <= 0 or dias_reales <= 0:
        print("Los días deben ser mayores que cero. Operación cancelada.")
        time.sleep(1)
        return

    prestamo = carros.crear_prestamo_carro_con_hotel(
        lista_de_prestamos,
        id_usuario,
        id_viaje,
        nombre_marca,
        dias_previstos,
        dias_reales,
        info_hospedaje
    )

    if prestamo is None:
        print("Ocurrió un problema al crear el préstamo del carro.")
        time.sleep(1)
        return

    print("\n--- Resumen del préstamo de carro ---")
    print("ID del préstamo:", prestamo["id_prestamo"])
    print("ID del usuario:", prestamo["id_usuario"])
    print("ID del viaje:", prestamo["id_viaje"])
    print("Marca del carro:", prestamo["marca"])
    print("Días previstos:", prestamo["dias_previstos"])
    print("Días reales:", prestamo["dias_reales"])
    print("Costo base del carro:", prestamo["costo_base_carro"], "EUR")
    print("Costo final del carro (con descuento/recargo):", prestamo["costo_final_carro"], "EUR")
    print("Hotel reservado (según destino):", prestamo["hotel_reservado"])
    print("Costo total de hotel:", prestamo["costo_hotel"], "EUR")
    print("Total a pagar (carro + hotel):", prestamo["total_pagar"], "EUR")

    if prestamo["entregado_a_tiempo"]:
        print("Se aplicó un DESCUENTO del 10% por entregar a tiempo.")
    else:
        print("Se aplicó un RECARGO del 15% por entrega tardía.")

    time.sleep(1)


def opcion_puntos_usuarios(lista_de_usuarios):
    """
    Gestiona los puntos y recompensas para un usuario.
    """
    print("\n--- Puntos y recompensas de usuario ---")

    if len(lista_de_usuarios) == 0:
        print("No hay usuarios registrados.")
        time.sleep(1)
        return

    print("\nUsuarios registrados:")
    for usuario in lista_de_usuarios:
        print(
            "ID:", usuario["id_usuario"],
            "| Nombre:", usuario["nombre"],
            "| Email:", usuario["email"]
        )

    id_usuario = input("Introduce el ID del usuario para gestionar sus puntos: ").strip()
    usuario_encontrado = usuarios.buscar_usuario_por_id(lista_de_usuarios, id_usuario)
    if usuario_encontrado is None:
        print("No existe un usuario con ese ID.")
        time.sleep(1)
        return

    puntos.menu_puntos_para_usuario(usuario_encontrado)
    time.sleep(1)


def opcion_beneficios_proveedores(lista_de_usuarios, lista_de_viajes, lista_de_reservas):
    """
    Gestiona los beneficios con proveedores (hoteles) para usuarios fieles.
    """
    print("\n--- Beneficios con proveedores (hoteles) ---")

    if len(lista_de_usuarios) == 0:
        print("No hay usuarios registrados.")
        time.sleep(1)
        return

    print("\nUsuarios registrados:")
    for usuario in lista_de_usuarios:
        print(
            "ID:", usuario["id_usuario"],
            "| Nombre:", usuario["nombre"],
            "| Email:", usuario["email"]
        )

    id_usuario = input("Introduce el ID del usuario para verificar beneficios con proveedores: ").strip()
    usuario_encontrado = usuarios.buscar_usuario_por_id(lista_de_usuarios, id_usuario)
    if usuario_encontrado is None:
        print("No existe un usuario con ese ID.")
        time.sleep(1)
        return

    proveedores.menu_beneficios_proveedores(
        usuario_encontrado,
        lista_de_viajes,
        lista_de_reservas
    )
    time.sleep(1)


def opcion_historial_usuario(
    lista_de_usuarios,
    lista_de_viajes,
    lista_de_reservas,
    lista_de_prestamos_carro,
    lista_movimientos_puntos,
    lista_beneficios_proveedores
):
    """
    Muestra el historial completo de un usuario:
    viajes, reservas, puntos, beneficios y descuentos.
    """
    print("\n--- Historial completo de usuario ---")

    if len(lista_de_usuarios) == 0:
        print("No hay usuarios registrados.")
        time.sleep(1)
        return

    print("\nUsuarios registrados:")
    for usuario in lista_de_usuarios:
        print(
            "ID:", usuario["id_usuario"],
            "| Nombre:", usuario["nombre"],
            "| Email:", usuario["email"]
        )

    id_usuario = input("Introduce el ID del usuario para ver su historial: ").strip()
    usuario_encontrado = usuarios.buscar_usuario_por_id(lista_de_usuarios, id_usuario)
    if usuario_encontrado is None:
        print("No existe un usuario con ese ID.")
        time.sleep(1)
        return

    historial.mostrar_historial_usuario(
        usuario_encontrado,
        lista_de_viajes,
        lista_de_reservas,
        lista_de_prestamos_carro,
        lista_movimientos_puntos,
        lista_beneficios_proveedores
    )
    time.sleep(1)


def main():
    """
    Función principal del programa.
    Carga los datos iniciales y muestra el menú hasta que el usuario decida salir.
    """
    print("Cargando datos de viajes y reservas desde archivos de texto...")
    lista_de_viajes = datos.leer_viajes(ARCHIVO_VIAJES)
    lista_de_reservas = datos.leer_reservas(ARCHIVO_RESERVAS)
    lista_de_usuarios = usuarios.leer_usuarios()
    lista_de_prestamos_carro = []          # Solo en memoria
    lista_movimientos_puntos = []          # Solo en memoria (rellénalo desde puntos.py si quieres)
    lista_beneficios_proveedores = []      # Solo en memoria (rellénalo desde proveedores.py si quieres)

    print("Viajes cargados:", len(lista_de_viajes))
    print("Reservas cargadas:", len(lista_de_reservas))
    print("Usuarios cargados:", len(lista_de_usuarios))
    time.sleep(1)

    opcion = ""

    while opcion != "13":
        mostrar_menu()
        opcion = input("Elige una opción (1-13): ").strip()

        if opcion == "1":
            mostrar_viajes_agrupados(lista_de_viajes, lista_de_reservas)
            time.sleep(1)
        elif opcion == "2":
            opcion_agregar_viaje(lista_de_viajes)
            time.sleep(1)
        elif opcion == "3":
            opcion_agregar_reserva(lista_de_viajes, lista_de_reservas)
            time.sleep(1)
        elif opcion == "4":
            opcion_ver_detalle_destino(lista_de_viajes)
            time.sleep(1)
        elif opcion == "5":
            lista_de_viajes, lista_de_reservas = opcion_limpiar_viajes(
                lista_de_viajes,
                lista_de_reservas
            )
            time.sleep(1)
        elif opcion == "6":
            opcion_generar_texto_redes(lista_de_viajes, lista_de_reservas)
            time.sleep(1)
        elif opcion == "7":
            opcion_comparar_moneda()
            time.sleep(1)
        elif opcion == "8":
            opcion_registrar_usuario(lista_de_usuarios)
            time.sleep(1)
        elif opcion == "9":
            opcion_rentar_carro(lista_de_usuarios, lista_de_viajes, lista_de_prestamos_carro)
            time.sleep(1)
        elif opcion == "10":
            opcion_puntos_usuarios(lista_de_usuarios)
            time.sleep(1)
        elif opcion == "11":
            opcion_beneficios_proveedores(lista_de_usuarios, lista_de_viajes, lista_de_reservas)
            time.sleep(1)
        elif opcion == "12":
            opcion_historial_usuario(
                lista_de_usuarios,
                lista_de_viajes,
                lista_de_reservas,
                lista_de_prestamos_carro,
                lista_movimientos_puntos,
                lista_beneficios_proveedores
            )
            time.sleep(1)
        elif opcion == "13":
            print("Saliendo del sistema. ¡Hasta pronto!")
            time.sleep(1)
        else:
            print("Opción no válida. Intenta de nuevo.")
            time.sleep(1)


if __name__ == "__main__":
    main()