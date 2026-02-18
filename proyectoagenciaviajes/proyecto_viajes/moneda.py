# Módulo para comparar la moneda natal con la moneda del país de visita
TASAS_CAMBIO = {
    # Europa
    "EUR": 1.0,    # Euro (zona euro)
    "GBP": 0.85,   # Libra esterlina (Reino Unido)
    "CHF": 0.95,   # Franco suizo (Suiza)
    "DKK": 7.45,   # Corona danesa (Dinamarca)
    "SEK": 11.2,   # Corona sueca (Suecia)
    "NOK": 11.0,   # Corona noruega (Noruega)
    "PLN": 4.2,    # Zloty (Polonia)
    "HUF": 400.0,  # Forinto (Hungría)
    "CZK": 25.0,   # Corona checa (Chequia)
    "RON": 5.0,    # Leu rumano (Rumanía)

    # América
    "USD": 1.1,    # Dólar estadounidense
    "CAD": 1.45,   # Dólar canadiense
    "MXN": 19.0,   # Peso mexicano
    "ARS": 950.0,  # Peso argentino
    "CLP": 1000.0, # Peso chileno
    "COP": 4500.0, # Peso colombiano
    "BRL": 6.0,    # Real brasileño
    "PEN": 4.0,    # Sol peruano
    "BOB": 7.5,    # Boliviano (Bolivia)

    # Asia
    "JPY": 160.0,  # Yen japonés
    "CNY": 7.8,    # Yuan chino
    "KRW": 1400.0, # Won surcoreano
    "INR": 90.0,   # Rupia india
    "THB": 38.0,   # Baht tailandés
    "IDR": 17000.0,# Rupia indonesia
    "SGD": 1.5,    # Dólar de Singapur
    "AED": 4.0,    # Dirham EAU (Dubái)

    # Oceanía
    "AUD": 1.6,    # Dólar australiano
    "NZD": 1.75,   # Dólar neozelandés

    # África y Medio Oriente
    "ZAR": 20.0,   # Rand sudafricano
    "MAD": 11.0,   # Dírham marroquí
    "EGP": 50.0,   # Libra egipcia
    "TRY": 35.0    # Lira turca
}


def obtener_tasa_moneda(codigo_moneda):
    """
    Devuelve la tasa de cambio de la moneda indicada
    respecto al euro (EUR).
    Si la moneda no existe, devuelve None.
    """
    codigo = codigo_moneda.strip().upper()
    if codigo in TASAS_CAMBIO:
        return TASAS_CAMBIO[codigo]
    else:
        return None


def convertir_moneda(codigo_origen, codigo_destino, cantidad):
    """
    Convierte una cantidad desde la moneda de origen
    a la moneda de destino usando las tasas del diccionario.
    Si alguna moneda no existe, devuelve None.
    """
    tasa_origen = obtener_tasa_moneda(codigo_origen)
    tasa_destino = obtener_tasa_moneda(codigo_destino)

    if tasa_origen is None or tasa_destino is None:
        return None

    cantidad_en_euros = cantidad / tasa_origen

    cantidad_destino = cantidad_en_euros * tasa_destino

    return cantidad_destino