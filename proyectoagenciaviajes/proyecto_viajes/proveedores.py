# proveedores.py
# Módulo para manejar vínculos con proveedores (hoteles) y
# aplicar descuentos a clientes fieles según sus reservas.

import hospedaje


def obtener_info_hotel_por_viaje(lista_de_viajes, id_viaje_buscar):
    """
    Dado un id_viaje, devuelve un diccionario con:
    - "viaje": datos del viaje
    - "hotel": datos del hotel (de hospedaje.py)
    o None si no se encuentra el viaje o el hotel.
    """
    viaje_encontrado = None
    for viaje in lista_de_viajes:
        if viaje["id_viaje"] == id_viaje_buscar:
            viaje_encontrado = viaje
            break

    if viaje_encontrado is None:
        return None

    destino = viaje_encontrado["destino"]
    info_hotel = hospedaje.obtener_hospedaje_por_destino(destino)

    if info_hotel is None:
        return None

    return {
        "viaje": viaje_encontrado,
        "hotel": info_hotel
    }


def contar_reservas_usuario_en_hotel(lista_de_viajes, lista_de_reservas, nombre_usuario, destino_objetivo):
    """
    Cuenta cuántas reservas ha hecho un usuario (por nombre)
    en viajes cuyo destino coincida con destino_objetivo.
    Se asume que cada destino tiene asociado un hotel proveedor.
    """
    nombre_normalizado = nombre_usuario.strip().lower()
    destino_normalizado = destino_objetivo.strip().lower()

    # Obtenemos todos los id_viaje que van a ese destino
    ids_viajes_destino = []
    for viaje in lista_de_viajes:
        if viaje["destino"].strip().lower() == destino_normalizado:
            ids_viajes_destino.append(viaje["id_viaje"])

    # Contamos las reservas del usuario en esos viajes
    contador = 0
    for reserva in lista_de_reservas:
        if (
            reserva["id_viaje"] in ids_viajes_destino and
            reserva["nombre_cliente"].strip().lower() == nombre_normalizado
        ):
            contador += 1

    return contador


def calcular_descuento_cliente_fiel(usuario, lista_de_viajes, lista_de_reservas, id_viaje_seleccionado):
    """
    Dado un usuario, las listas de viajes y reservas, y un id_viaje,
    calcula si el usuario es cliente fiel del hotel asociado a ese destino.

    Regla:
    - Si tiene 3 o 4 reservas en ese destino -> 5% de descuento.
    - Si tiene 5 o más reservas en ese destino -> 7% de descuento.
    - Si tiene menos de 3 reservas -> 0% (no es cliente fiel).

    Devuelve un diccionario con:
    - "aplica": True/False
    - "porcentaje": 0, 5 o 7
    - "total_reservas_hotel": número de reservas encontradas
    - "nombre_hotel": nombre del hotel
    - "destino": destino del viaje
    """
    info = obtener_info_hotel_por_viaje(lista_de_viajes, id_viaje_seleccionado)
    if info is None:
        return {
            "aplica": False,
            "porcentaje": 0,
            "total_reservas_hotel": 0,
            "nombre_hotel": None,
            "destino": None
        }

    viaje = info["viaje"]
    hotel = info["hotel"]

    destino = viaje["destino"]
    nombre_hotel = hotel["hotel"]

    # Contamos reservas del usuario en ese destino/hotel
    total_reservas = contar_reservas_usuario_en_hotel(
        lista_de_viajes,
        lista_de_reservas,
        usuario["nombre"],
        destino
    )

    if total_reservas >= 5:
        porcentaje = 7
    elif total_reservas >= 3:
        porcentaje = 5
    else:
        porcentaje = 0

    aplica = porcentaje > 0

    return {
        "aplica": aplica,
        "porcentaje": porcentaje,
        "total_reservas_hotel": total_reservas,
        "nombre_hotel": nombre_hotel,
        "destino": destino
    }