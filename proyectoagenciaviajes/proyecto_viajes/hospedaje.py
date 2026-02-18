# hospedaje.py
# Este módulo contiene información de hospedaje y restaurantes
# asociada a cada destino (ciudad).
# La información está en memoria usando diccionarios sencillos.

# Diccionario donde la clave es el nombre del destino (texto)
# y el valor es otro diccionario con datos de hotel y restaurante.
DATOS_HOSPEDAJE = {
    "Madrid": {
        "hotel": "Hotel Sol de Madrid",
        "precio_noche": 80.0,
        "restaurante": "Restaurante La Plaza",
        "precio_plato_dia": 15.0
    },
    "París": {
        "hotel": "Hotel París Lumière",
        "precio_noche": 120.0,
        "restaurante": "Bistró La Tour",
        "precio_plato_dia": 20.0
    },
    "Roma": {
        "hotel": "Hotel Colosseo",
        "precio_noche": 90.0,
        "restaurante": "Trattoria Roma",
        "precio_plato_dia": 18.0
    },
    "Londres": {
        "hotel": "Hotel London Bridge",
        "precio_noche": 130.0,
        "restaurante": "The River Restaurant",
        "precio_plato_dia": 22.0
    },
    "Barcelona": {
        "hotel": "Hotel Mar Azul Barcelona",
        "precio_noche": 85.0,
        "restaurante": "Tapas del Puerto",
        "precio_plato_dia": 16.0
    },
    "Berlín": {
        "hotel": "Hotel Muro de Berlín",
        "precio_noche": 95.0,
        "restaurante": "Café Alexanderplatz",
        "precio_plato_dia": 17.0
    },
    "Ámsterdam": {
        "hotel": "Hotel Canal View",
        "precio_noche": 110.0,
        "restaurante": "Restaurante Tulipán",
        "precio_plato_dia": 19.0
    },
    "Lisboa": {
        "hotel": "Hotel Mirador de Lisboa",
        "precio_noche": 75.0,
        "restaurante": "Casa del Bacalao",
        "precio_plato_dia": 14.0
    },
    "Nueva York": {
        "hotel": "Hotel Times Square",
        "precio_noche": 180.0,
        "restaurante": "Broadway Diner",
        "precio_plato_dia": 25.0
    },
    "Los Ángeles": {
        "hotel": "Sunset Boulevard Hotel",
        "precio_noche": 170.0,
        "restaurante": "Hollywood Grill",
        "precio_plato_dia": 24.0
    },
    "Miami": {
        "hotel": "Miami Beach Resort",
        "precio_noche": 150.0,
        "restaurante": "Ocean Breeze Restaurant",
        "precio_plato_dia": 22.0
    },
    "Ciudad de México": {
        "hotel": "Hotel Zócalo Central",
        "precio_noche": 70.0,
        "restaurante": "Restaurante La Hacienda",
        "precio_plato_dia": 12.0
    },
    "Buenos Aires": {
        "hotel": "Hotel Obelisco",
        "precio_noche": 65.0,
        "restaurante": "Parrilla San Telmo",
        "precio_plato_dia": 13.0
    },
    "Santiago": {
        "hotel": "Hotel Cordillera",
        "precio_noche": 68.0,
        "restaurante": "Sabores de Chile",
        "precio_plato_dia": 12.5
    },
    "Lima": {
        "hotel": "Hotel Costa del Pacífico",
        "precio_noche": 60.0,
        "restaurante": "Cevichería El Puerto",
        "precio_plato_dia": 11.0
    },
    "Bogotá": {
        "hotel": "Hotel Montaña Andina",
        "precio_noche": 62.0,
        "restaurante": "Ajiaco Tradicional",
        "precio_plato_dia": 10.5
    },
    "Río de Janeiro": {
        "hotel": "Hotel Copacabana Vista",
        "precio_noche": 100.0,
        "restaurante": "Churrasquería del Mar",
        "precio_plato_dia": 18.0
    },
    "São Paulo": {
        "hotel": "Hotel Paulista Center",
        "precio_noche": 90.0,
        "restaurante": "Restaurante Jardins",
        "precio_plato_dia": 16.5
    },
    "Toronto": {
        "hotel": "Hotel CN Tower View",
        "precio_noche": 130.0,
        "restaurante": "Maple Leaf Bistro",
        "precio_plato_dia": 21.0
    },
    "Vancouver": {
        "hotel": "Hotel Pacific Harbor",
        "precio_noche": 125.0,
        "restaurante": "Salmon & Co.",
        "precio_plato_dia": 20.0
    },
    "Tokio": {
        "hotel": "Hotel Shibuya Lights",
        "precio_noche": 160.0,
        "restaurante": "Sushi Sakura",
        "precio_plato_dia": 23.0
    },
    "Kioto": {
        "hotel": "Ryokan Jardín Zen",
        "precio_noche": 140.0,
        "restaurante": "Casa del Té Hanami",
        "precio_plato_dia": 20.0
    },
    "Osaka": {
        "hotel": "Hotel Castillo Osaka",
        "precio_noche": 135.0,
        "restaurante": "Okonomiyaki House",
        "precio_plato_dia": 19.5
    },
    "Seúl": {
        "hotel": "Hotel Gangnam Sky",
        "precio_noche": 150.0,
        "restaurante": "Kimchi & BBQ",
        "precio_plato_dia": 19.0
    },
    "Pekín": {
        "hotel": "Hotel Muro Imperial",
        "precio_noche": 120.0,
        "restaurante": "Pato Laqueado Real",
        "precio_plato_dia": 18.0
    },
    "Shanghái": {
        "hotel": "Hotel Bund River",
        "precio_noche": 130.0,
        "restaurante": "Noodles del Dragón",
        "precio_plato_dia": 17.5
    },
    "Bangkok": {
        "hotel": "Hotel Río Chao Phraya",
        "precio_noche": 80.0,
        "restaurante": "Thai Spice Restaurant",
        "precio_plato_dia": 13.0
    },
    "Singapur": {
        "hotel": "Hotel Marina View",
        "precio_noche": 170.0,
        "restaurante": "Orchard Street Food",
        "precio_plato_dia": 21.0
    },
    "Sídney": {
        "hotel": "Hotel Opera Bay",
        "precio_noche": 160.0,
        "restaurante": "Harbour Seafood",
        "precio_plato_dia": 22.0
    },
    "Melbourne": {
        "hotel": "Hotel Yarra Riverside",
        "precio_noche": 150.0,
        "restaurante": "Café Federation",
        "precio_plato_dia": 20.0
    },
    "Auckland": {
        "hotel": "Hotel Sky Tower",
        "precio_noche": 140.0,
        "restaurante": "Kiwi Taste",
        "precio_plato_dia": 19.0
    },
    "Dubái": {
        "hotel": "Hotel Marina Dunes",
        "precio_noche": 200.0,
        "restaurante": "Oasis Gourmet",
        "precio_plato_dia": 26.0
    },
    "Estambul": {
        "hotel": "Hotel Bósforo Palace",
        "precio_noche": 110.0,
        "restaurante": "Sabores del Bazar",
        "precio_plato_dia": 17.0
    },
    "Atenas": {
        "hotel": "Hotel Acrópolis View",
        "precio_noche": 95.0,
        "restaurante": "Taverna Helénica",
        "precio_plato_dia": 16.0
    },
    "Viena": {
        "hotel": "Hotel Danubio Real",
        "precio_noche": 120.0,
        "restaurante": "Café Sacherplatz",
        "precio_plato_dia": 19.0
    },
    "Praga": {
        "hotel": "Hotel Puente Carlos",
        "precio_noche": 100.0,
        "restaurante": "Cerveza y Goulash",
        "precio_plato_dia": 16.5
    },
    "Budapest": {
        "hotel": "Hotel Termas del Danubio",
        "precio_noche": 90.0,
        "restaurante": "Paprika Bistro",
        "precio_plato_dia": 15.0
    },
    "Varsovia": {
        "hotel": "Hotel Plaza Real",
        "precio_noche": 85.0,
        "restaurante": "Pierogi House",
        "precio_plato_dia": 14.5
    },
    "Copenhague": {
        "hotel": "Hotel Sirena del Norte",
        "precio_noche": 140.0,
        "restaurante": "Smorrebrod Café",
        "precio_plato_dia": 21.0
    },
    "Estocolmo": {
        "hotel": "Hotel Islas del Norte",
        "precio_noche": 135.0,
        "restaurante": "Salmon & Fjords",
        "precio_plato_dia": 20.0
    },
    "Oslo": {
        "hotel": "Hotel Bosque Nórdico",
        "precio_noche": 130.0,
        "restaurante": "Vikingo Grill",
        "precio_plato_dia": 20.0
    },
    "Helsinki": {
        "hotel": "Hotel Lago Helado",
        "precio_noche": 125.0,
        "restaurante": "Sauna Bistro",
        "precio_plato_dia": 19.0
    },
    "Zúrich": {
        "hotel": "Hotel Lago Zúrich",
        "precio_noche": 170.0,
        "restaurante": "Fondue Chalet",
        "precio_plato_dia": 24.0
    },
    "Ginebra": {
        "hotel": "Hotel Reloj Suizo",
        "precio_noche": 165.0,
        "restaurante": "Chocolate & Cheese",
        "precio_plato_dia": 23.0
    },
    "Bruselas": {
        "hotel": "Hotel Gran Plaza",
        "precio_noche": 120.0,
        "restaurante": "Waffles & Beer",
        "precio_plato_dia": 18.0
    },
    "Dublín": {
        "hotel": "Hotel Temple Bar",
        "precio_noche": 110.0,
        "restaurante": "Irish Stew House",
        "precio_plato_dia": 17.0
    },
    "Edimburgo": {
        "hotel": "Hotel Castillo de Edimburgo",
        "precio_noche": 115.0,
        "restaurante": "Highland Flavours",
        "precio_plato_dia": 18.0
    },
    "Marrakech": {
        "hotel": "Riad Jardín del Desierto",
        "precio_noche": 70.0,
        "restaurante": "Tagine Tradicional",
        "precio_plato_dia": 13.0
    },
    "El Cairo": {
        "hotel": "Hotel Pirámides de Giza",
        "precio_noche": 75.0,
        "restaurante": "Nilo Restaurante",
        "precio_plato_dia": 12.5
    },
    "Johannesburgo": {
        "hotel": "Hotel Savanna City",
        "precio_noche": 80.0,
        "restaurante": "Safari Grill",
        "precio_plato_dia": 14.0
    },
    "Ciudad del Cabo": {
        "hotel": "Hotel Table Mountain",
        "precio_noche": 95.0,
        "restaurante": "Cape Seafood",
        "precio_plato_dia": 16.0
    },
    "Nueva Delhi": {
        "hotel": "Hotel Puerta de la India",
        "precio_noche": 65.0,
        "restaurante": "Curry Mahal",
        "precio_plato_dia": 11.0
    },
    "Bali": {
        "hotel": "Resort Playa de Bali",
        "precio_noche": 90.0,
        "restaurante": "Templo del Coco",
        "precio_plato_dia": 14.5
    }
}


def obtener_hospedaje_por_destino(nombre_destino):
    """
    Devuelve la información de hospedaje (hotel y restaurante)
    para un destino concreto.
    La comparación se hace sin importar mayúsculas o minúsculas.
    Si el destino no existe en el diccionario, devuelve None.
    """
    if nombre_destino is None:
        return None

    
    destino_normalizado = nombre_destino.strip().lower()

    for clave_destino in DATOS_HOSPEDAJE:
        clave_normalizada = clave_destino.strip().lower()
        if destino_normalizado == clave_normalizada:
            return DATOS_HOSPEDAJE[clave_destino]
        
    return None