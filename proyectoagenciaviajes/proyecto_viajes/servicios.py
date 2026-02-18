# servicios.py
# Este módulo contiene la lógica del negocio:
# - Agrupar reservas por viaje
# - Limpiar viajes pasados
# - Generar textos para redes
# - Crear nuevas reservas y viajes en memoria

from datetime import datetime


def agrupar_reservas_por_viaje(lista_de_viajes, lista_de_reservas):
    """
    Recibe listas de viajes y reservas y devuelve un diccionario
    donde la clave es el id_viaje y el valor es otro diccionario con:
    - "viaje": información del viaje
    - "reservas": lista de reservas de ese viaje
    - "total_plazas": suma de plazas reservadas
    """
    agrupado = {}

    # Primero añadimos todos los viajes al diccionario
    for viaje in lista_de_viajes:
        id_viaje = viaje["id_viaje"]
        agrupado[id_viaje] = {
            "viaje": viaje,
            "reservas": [],
            "total_plazas": 0
        }

    # Luego añadimos las reservas al viaje correspondiente
    for reserva in lista_de_reservas:
        id_viaje_reserva = reserva["id_viaje"]

        # Verificamos que el viaje exista en la lista de viajes
        if id_viaje_reserva in agrupado:
            agrupado[id_viaje_reserva]["reservas"].append(reserva)
            agrupado[id_viaje_reserva]["total_plazas"] += reserva["plazas"]

    return agrupado


def convertir_texto_a_fecha(texto_fecha):
    """
    Convierte una fecha en texto con formato 'dd/mm/aaaa'
    a un objeto de tipo date de Python.
    Si el texto no tiene el formato correcto, devuelve None.
    """
    try:
        momento = datetime.strptime(texto_fecha, "%d/%m/%Y")
        return momento.date()
    except Exception:
        return None


def limpiar_viajes_pasados(lista_de_viajes, lista_de_reservas, fecha_hoy):
    """
    Elimina de la lista de viajes aquellos cuya fecha_fin ya pasó
    (es anterior a la fecha de hoy).
    También elimina las reservas asociadas a esos viajes.
    Devuelve dos nuevas listas: (nuevos_viajes, nuevas_reservas).
    """
    nuevos_viajes = []
    ids_viajes_activos = []

    # Filtramos viajes que aún no han terminado
    for viaje in lista_de_viajes:
        fecha_fin_texto = viaje["fecha_fin"]
        fecha_fin = convertir_texto_a_fecha(fecha_fin_texto)

        if fecha_fin is None:
            # Si no podemos leer la fecha, por seguridad consideramos que sigue activo
            nuevos_viajes.append(viaje)
            ids_viajes_activos.append(viaje["id_viaje"])
        else:
            # Solo mantenemos viajes cuya fecha_fin es hoy o en el futuro
            if fecha_fin >= fecha_hoy:
                nuevos_viajes.append(viaje)
                ids_viajes_activos.append(viaje["id_viaje"])

    # Ahora filtramos las reservas que pertenecen a viajes activos
    nuevas_reservas = []
    for reserva in lista_de_reservas:
        if reserva["id_viaje"] in ids_viajes_activos:
            nuevas_reservas.append(reserva)

    return nuevos_viajes, nuevas_reservas


def buscar_viaje_por_id(lista_de_viajes, id_viaje_buscar):
    """
    Busca un viaje en la lista por su id_viaje.
    Si lo encuentra, devuelve el diccionario del viaje.
    Si no existe, devuelve None.
    """
    for viaje in lista_de_viajes:
        if viaje["id_viaje"] == id_viaje_buscar:
            return viaje
    return None


def generar_texto_redes_para_viaje(viaje, total_reservas):
    """
    Recibe un diccionario 'viaje' y el número total de plazas reservadas.
    Devuelve un texto simple que podría publicarse en redes sociales.
    """
    destino = viaje["destino"]
    fecha_inicio = viaje["fecha_inicio"]
    fecha_fin = viaje["fecha_fin"]
    precio = viaje["precio"]

    mensaje = (
        f"¡Descubre nuestro viaje a {destino}! "
        f"Del {fecha_inicio} al {fecha_fin}, "
        f"por solo {precio:.2f} EUR por persona. "
        f"Ya tenemos {total_reservas} plazas reservadas. "
        "¡Reserva la tuya hoy mismo con la agencia El guerrero del camino!"
    )

    return mensaje


def generar_nueva_reserva_en_memoria(lista_de_reservas, id_viaje, nombre_cliente, plazas):
    """
    Crea una nueva reserva como diccionario y la añade a la lista de reservas.
    Calcula un nuevo id_reserva basado en las reservas existentes.
    Devuelve la nueva reserva creada.
    """
    # Calculamos el siguiente id_reserva como número entero
    max_id = 0
    for reserva in lista_de_reservas:
        try:
            valor = int(reserva["id_reserva"])
            if valor > max_id:
                max_id = valor
        except ValueError:
            # Si algún id no es numérico, lo ignoramos
            continue

    nuevo_id = max_id + 1
    id_reserva_texto = str(nuevo_id)

    nueva_reserva = {
        "id_reserva": id_reserva_texto,
        "id_viaje": id_viaje,
        "nombre_cliente": nombre_cliente,
        "plazas": plazas
    }

    lista_de_reservas.append(nueva_reserva)

    return nueva_reserva


def contar_plazas_reservadas_para_viaje(lista_de_reservas, id_viaje):
    """
    Cuenta cuántas plazas están reservadas para un viaje concreto.
    Devuelve un número entero.
    """
    total = 0
    for reserva in lista_de_reservas:
        if reserva["id_viaje"] == id_viaje:
            total += reserva["plazas"]
    return total


def generar_nuevo_viaje_en_memoria(lista_de_viajes, destino, fecha_inicio, fecha_fin, precio):
    """
    Crea un nuevo viaje como diccionario y lo añade a la lista de viajes.
    Calcula un nuevo id_viaje basado en los viajes existentes.
    Devuelve el nuevo viaje creado.
    """
    max_id = 0
    for viaje in lista_de_viajes:
        try:
            valor = int(viaje["id_viaje"])
            if valor > max_id:
                max_id = valor
        except ValueError:
            # Si algún id no es numérico, lo ignoramos
            continue

    nuevo_id = max_id + 1
    id_viaje_texto = str(nuevo_id)

    nuevo_viaje = {
        "id_viaje": id_viaje_texto,
        "destino": destino,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "precio": precio
    }

    lista_de_viajes.append(nuevo_viaje)

    return nuevo_viaje


def contar_plazas_reservadas_para_viaje(lista_de_reservas, id_viaje):
    """
    Cuenta cuántas plazas están reservadas para un viaje concreto.
    Devuelve un número entero.
    """
    total = 0
    for reserva in lista_de_reservas:
        if reserva["id_viaje"] == id_viaje:
            total += reserva["plazas"]
    return total