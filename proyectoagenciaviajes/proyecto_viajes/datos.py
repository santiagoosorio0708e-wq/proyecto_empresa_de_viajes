# Este módulo contiene funciones simples para leer y escribir

def leer_viajes(ruta_archivo_viajes):
    """
    Lee el archivo de viajes y devuelve una lista de diccionarios.
    Cada línea del archivo debe tener el formato:
    id_viaje,destino,fecha_inicio,fecha_fin,precio
    """
    lista_de_viajes = []

    try:
        archivo_viajes = open(ruta_archivo_viajes, "r", encoding="utf-8")
        for linea in archivo_viajes:
            linea = linea.strip()

            if linea == "" or linea.startswith("#"):
                continue

            partes = linea.split(",")

            if len(partes) != 5:
                continue

            id_viaje = partes[0]
            destino = partes[1]
            fecha_inicio = partes[2]
            fecha_fin = partes[3]

            try:
                precio = float(partes[4])
            except ValueError:
                precio = 0.0

            viaje = {
                "id_viaje": id_viaje,
                "destino": destino,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "precio": precio
            }

            lista_de_viajes.append(viaje)

        archivo_viajes.close()
    except FileNotFoundError:
        print("Aviso: No se encontró el archivo de viajes:", ruta_archivo_viajes)
    except Exception as error:
        print("Error al leer el archivo de viajes:", error)

    return lista_de_viajes


def leer_reservas(ruta_archivo_reservas):
    """
    Lee el archivo de reservas y devuelve una lista de diccionarios.
    Cada línea del archivo debe tener el formato:
    id_reserva,id_viaje,nombre_cliente,plazas
    """
    lista_de_reservas = []

    try:
        archivo_reservas = open(ruta_archivo_reservas, "r", encoding="utf-8")
        for linea in archivo_reservas:
            linea = linea.strip()

            if linea == "" or linea.startswith("#"):
                continue

            partes = linea.split(",")

            if len(partes) != 4:
                continue

            id_reserva = partes[0]
            id_viaje = partes[1]
            nombre_cliente = partes[2]

            try:
                plazas = int(partes[3])
            except ValueError:
                plazas = 0

            reserva = {
                "id_reserva": id_reserva,
                "id_viaje": id_viaje,
                "nombre_cliente": nombre_cliente,
                "plazas": plazas
            }

            lista_de_reservas.append(reserva)

        archivo_reservas.close()
    except FileNotFoundError:
        print("Aviso: No se encontró el archivo de reservas:", ruta_archivo_reservas)
    except Exception as error:
        print("Error al leer el archivo de reservas:", error)

    return lista_de_reservas


def guardar_viajes(ruta_archivo_viajes, lista_de_viajes):
    """
    Guarda la lista de viajes en el archivo indicado.
    Cada viaje se escribe en una línea con el formato:
    id_viaje,destino,fecha_inicio,fecha_fin,precio
    """
    try:
        archivo_viajes = open(ruta_archivo_viajes, "w", encoding="utf-8")

        for viaje in lista_de_viajes:
            linea = (
                viaje["id_viaje"] + "," +
                viaje["destino"] + "," +
                viaje["fecha_inicio"] + "," +
                viaje["fecha_fin"] + "," +
                str(viaje["precio"])
            )
            archivo_viajes.write(linea + "\n")

        archivo_viajes.close()
    except Exception as error:
        print("Error al guardar el archivo de viajes:", error)


def guardar_reservas(ruta_archivo_reservas, lista_de_reservas):
    """
    Guarda la lista de reservas en el archivo indicado.
    Cada reserva se escribe en una línea con el formato:
    id_reserva,id_viaje,nombre_cliente,plazas
    """
    try:
        archivo_reservas = open(ruta_archivo_reservas, "w", encoding="utf-8")

        for reserva in lista_de_reservas:
            linea = (
                reserva["id_reserva"] + "," +
                reserva["id_viaje"] + "," +
                reserva["nombre_cliente"] + "," +
                str(reserva["plazas"])
            )
            archivo_reservas.write(linea + "\n")

        archivo_reservas.close()
    except Exception as error:
        print("Error al guardar el archivo de reservas:", error)


def agregar_reserva_en_archivo(ruta_archivo_reservas, nueva_reserva):
    """
    Agrega una nueva reserva al final del archivo de reservas.
    No borra el contenido anterior, solo añade una nueva línea.
    """
    try:
        archivo_reservas = open(ruta_archivo_reservas, "a", encoding="utf-8")

        linea = (
            nueva_reserva["id_reserva"] + "," +
            nueva_reserva["id_viaje"] + "," +
            nueva_reserva["nombre_cliente"] + "," +
            str(nueva_reserva["plazas"])
        )
        archivo_reservas.write(linea + "\n")

        archivo_reservas.close()
    except Exception as error:
        print("Error al agregar la reserva en el archivo:", error)


def agregar_viaje_en_archivo(ruta_archivo_viajes, nuevo_viaje):
    """
    Agrega un nuevo viaje al final del archivo de viajes.
    No borra el contenido anterior, solo añade una nueva línea.
    Formato:
    id_viaje,destino,fecha_inicio,fecha_fin,precio
    """
    try:
        archivo_viajes = open(ruta_archivo_viajes, "a", encoding="utf-8")

        linea = (
            nuevo_viaje["id_viaje"] + "," +
            nuevo_viaje["destino"] + "," +
            nuevo_viaje["fecha_inicio"] + "," +
            nuevo_viaje["fecha_fin"] + "," +
            str(nuevo_viaje["precio"])
        )
        archivo_viajes.write(linea + "\n")

        archivo_viajes.close()
    except Exception as error:
        print("Error al agregar el viaje en el archivo:", error)