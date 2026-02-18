# Módulo para gestionar el préstamo (renta) de carros
MARCAS_CARRO = {
    "TOYOTA": 50.0,
    "HONDA": 48.0,
    "FORD": 52.0,
    "CHEVROLET": 50.0,
    "NISSAN": 47.0,
    "BMW": 80.0,
    "MERCEDES": 85.0,
    "AUDI": 78.0,
    "KIA": 45.0,
    "HYUNDAI": 46.0,
    "VOLKSWAGEN": 49.0,
    "RENAULT": 44.0,
    "PEUGEOT": 43.0,
    "FIAT": 40.0,
    "JEEP": 70.0,
    "LAND ROVER": 90.0,
    "VOLVO": 75.0,
    "TESLA": 95.0,
    "MAZDA": 48.0,
    "SUBARU": 50.0
}


def normalizar_texto(texto):
    """
    Quita espacios al inicio y final y convierte a mayúsculas.
    Sirve para comparar marcas sin importar mayúsculas/minúsculas.
    """
    return texto.strip().upper()


def obtener_precio_base_marca(nombre_marca):
    """
    Devuelve el precio base por día de la marca indicada.
    Si la marca no existe, devuelve None.
    """
    clave = normalizar_texto(nombre_marca)
    if clave in MARCAS_CARRO:
        return MARCAS_CARRO[clave]
    else:
        return None


def calcular_costo_carro(precio_base_dia, dias_previstos, dias_reales):
    """
    Calcula el costo del préstamo del carro.
    - Si se entrega en el tiempo acordado (dias_reales <= dias_previstos):
        se hace un DESCUENTO del 10% sobre el costo base.
    - Si se entrega tarde (dias_reales > dias_previstos):
        se AUMENTA un 15% sobre el costo base.
    Devuelve una tupla:
    (costo_base, costo_final, entregado_a_tiempo)
    """
    costo_base = precio_base_dia * dias_previstos

    if dias_reales <= dias_previstos:
        # Descuento del 10%
        costo_final = costo_base * 0.90
        entregado_a_tiempo = True
    else:
        # Recargo del 15%
        costo_final = costo_base * 1.15
        entregado_a_tiempo = False

    return costo_base, costo_final, entregado_a_tiempo


def calcular_costo_hotel(precio_noche, dias_estadia):
    """
    Calcula el costo total del hotel:
    precio por noche * número de días de estancia.
    """
    return precio_noche * dias_estadia


def crear_prestamo_carro_con_hotel(
    lista_de_prestamos,
    id_usuario,
    id_viaje,
    nombre_marca,
    dias_previstos,
    dias_reales,
    info_hospedaje
):
    """
    Crea un nuevo registro de préstamo de carro ligado a:
    - Un usuario (id_usuario)
    - Un viaje (id_viaje)
    - Una marca de carro (nombre_marca)
    - La reserva de hotel para el mismo destino (info_hospedaje)
    Aplica:
    - Descuento del 10% si se entrega a tiempo.
    - Recargo del 15% si se entrega tarde.
    Devuelve un diccionario con toda la información del préstamo.
    """
    # Precio base de la marca
    precio_base_dia = obtener_precio_base_marca(nombre_marca)
    if precio_base_dia is None:
        return None  # Marca no válida

    # Calculamos el costo del carro
    costo_base_carro, costo_final_carro, entregado_a_tiempo = calcular_costo_carro(
        precio_base_dia,
        dias_previstos,
        dias_reales
    )

    # Calculamos el costo del hotel si hay información
    if info_hospedaje is not None:
        precio_noche = info_hospedaje["precio_noche"]
        costo_hotel = calcular_costo_hotel(precio_noche, dias_previstos)
        nombre_hotel = info_hospedaje["hotel"]
    else:
        costo_hotel = 0.0
        nombre_hotel = "Sin información de hotel"

    total_pagar = costo_final_carro + costo_hotel

    # Calculamos un nuevo id_prestamo a partir de la lista existente
    max_id = 0
    for prestamo in lista_de_prestamos:
        try:
            valor = int(prestamo["id_prestamo"])
            if valor > max_id:
                max_id = valor
        except ValueError:
            continue

    nuevo_id = max_id + 1
    id_prestamo_texto = str(nuevo_id)

    prestamo = {
        "id_prestamo": id_prestamo_texto,
        "id_usuario": id_usuario,
        "id_viaje": id_viaje,
        "marca": normalizar_texto(nombre_marca),
        "dias_previstos": dias_previstos,
        "dias_reales": dias_reales,
        "costo_base_carro": costo_base_carro,
        "costo_final_carro": costo_final_carro,
        "costo_hotel": costo_hotel,
        "total_pagar": total_pagar,
        "entregado_a_tiempo": entregado_a_tiempo,
        "hotel_reservado": nombre_hotel
    }

    lista_de_prestamos.append(prestamo)

    return prestamo