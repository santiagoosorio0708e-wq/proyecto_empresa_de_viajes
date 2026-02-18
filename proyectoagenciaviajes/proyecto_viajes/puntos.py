# puntos.py
# Módulo para manejar puntos de recompensa de los usuarios.
# Permite:
# - Guardar y cargar puntos desde un archivo de texto.
# - Consultar el saldo total de puntos de un usuario.
# - Usar (gastar) puntos.
# - Mostrar un pequeño historial de puntos ganados y usados.


ARCHIVO_PUNTOS = "puntos_usuarios.txt"


def leer_puntos():
    """
    Lee el archivo de puntos y devuelve una lista de diccionarios.
    Formato de cada línea:
    id_usuario,puntos_totales,puntos_ganados,puntos_usados
    Si el archivo no existe, devuelve una lista vacía.
    """
    lista_puntos = []

    try:
        archivo = open(ARCHIVO_PUNTOS, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()

            if linea == "" or linea.startswith("#"):
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            id_usuario = partes[0]

            try:
                puntos_totales = int(partes[1])
            except ValueError:
                puntos_totales = 0

            try:
                puntos_ganados = int(partes[2])
            except ValueError:
                puntos_ganados = 0

            try:
                puntos_usados = int(partes[3])
            except ValueError:
                puntos_usados = 0

            registro = {
                "id_usuario": id_usuario,
                "puntos_totales": puntos_totales,
                "puntos_ganados": puntos_ganados,
                "puntos_usados": puntos_usados,
            }
            lista_puntos.append(registro)

        archivo.close()
    except FileNotFoundError:
        # Si no existe el archivo, simplemente devolvemos lista vacía
        lista_puntos = []
    except Exception as error:
        print("Error al leer el archivo de puntos:", error)

    return lista_puntos


def guardar_puntos(lista_puntos):
    """
    Guarda la lista de puntos en el archivo de texto.
    Sobrescribe por completo el archivo.
    Formato de cada línea:
    id_usuario,puntos_totales,puntos_ganados,puntos_usados
    """
    try:
        archivo = open(ARCHIVO_PUNTOS, "w", encoding="utf-8")

        for registro in lista_puntos:
            linea = (
                registro["id_usuario"] + "," +
                str(registro["puntos_totales"]) + "," +
                str(registro["puntos_ganados"]) + "," +
                str(registro["puntos_usados"])
            )
            archivo.write(linea + "\n")

        archivo.close()
    except Exception as error:
        print("Error al guardar el archivo de puntos:", error)


def buscar_registro_por_usuario(lista_puntos, id_usuario):
    """
    Busca el registro de puntos de un usuario por su id_usuario.
    Si existe, lo devuelve.
    Si no existe, devuelve None.
    """
    for registro in lista_puntos:
        if registro["id_usuario"] == id_usuario:
            return registro
    return None


def obtener_o_crear_registro(lista_puntos, id_usuario):
    """
    Devuelve el registro de puntos de un usuario.
    Si no existe, crea uno nuevo con 0 puntos y lo añade a la lista.
    """
    registro = buscar_registro_por_usuario(lista_puntos, id_usuario)
    if registro is not None:
        return registro

    # Crear nuevo registro con 0 puntos
    nuevo = {
        "id_usuario": id_usuario,
        "puntos_totales": 0,
        "puntos_ganados": 0,
        "puntos_usados": 0,
    }
    lista_puntos.append(nuevo)
    return nuevo


def agregar_puntos(id_usuario, cantidad, lista_puntos):
    """
    Suma 'cantidad' de puntos al usuario indicado.
    Actualiza puntos_totales y puntos_ganados.
    'cantidad' debe ser un entero positivo.
    """
    if cantidad <= 0:
        return

    registro = obtener_o_crear_registro(lista_puntos, id_usuario)
    registro["puntos_totales"] += cantidad
    registro["puntos_ganados"] += cantidad


def usar_puntos(id_usuario, cantidad, lista_puntos):
    """
    Resta 'cantidad' de puntos al usuario indicado.
    Actualiza puntos_totales y puntos_usados.
    Devuelve True si se pudieron usar los puntos, False en caso contrario.
    """
    if cantidad <= 0:
        return False

    registro = obtener_o_crear_registro(lista_puntos, id_usuario)

    if cantidad > registro["puntos_totales"]:
        return False

    registro["puntos_totales"] -= cantidad
    registro["puntos_usados"] += cantidad
    return True


def mostrar_resumen_puntos(registro, nombre_usuario):
    """
    Muestra por pantalla un resumen simple del estado de puntos
    de un usuario.
    """
    print("\n===== Resumen de puntos para:", nombre_usuario, "=====")
    print("ID de usuario:", registro["id_usuario"])
    print("Puntos totales actuales:", registro["puntos_totales"])
    print("Puntos ganados (histórico):", registro["puntos_ganados"])
    print("Puntos usados (histórico):", registro["puntos_usados"])
    print("==============================================")


def menu_puntos_para_usuario(usuario):
    """
    Muestra un pequeño menú de puntos para un usuario concreto.
    Esta es la función que llama main.py: puntos.menu_puntos_para_usuario(usuario_encontrado)

    El parámetro 'usuario' debe ser un diccionario que tenga al menos:
    - 'id_usuario'
    - 'nombre'
    """
    # Cargamos todos los registros de puntos
    lista_puntos = leer_puntos()

    # Aseguramos que el usuario tenga un registro
    id_usuario = usuario["id_usuario"]
    nombre_usuario = usuario["nombre"]
    registro = obtener_o_crear_registro(lista_puntos, id_usuario)

    opcion = ""

    while opcion != "4":
        print("\n========== Menú de puntos para", nombre_usuario, "==========")
        print("1. Ver saldo total y resumen de puntos")
        print("2. Usar puntos ahora")
        print("3. Acumular puntos (simulación de puntos ganados)")
        print("4. Volver al menú principal")
        print("===================================================")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            # Mostrar resumen
            mostrar_resumen_puntos(registro, nombre_usuario)

        elif opcion == "2":
            # Usar puntos
            print("\n--- Usar puntos ---")
            print("Puntos disponibles actualmente:", registro["puntos_totales"])
            cantidad_texto = input("¿Cuántos puntos quieres usar?: ").strip()
            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            exito = usar_puntos(id_usuario, cantidad, lista_puntos)
            if exito:
                print("Puntos usados correctamente.")
            else:
                print("No tienes suficientes puntos para usar esa cantidad.")

            # Actualizamos el registro local después de usar puntos
            registro = buscar_registro_por_usuario(lista_puntos, id_usuario)
            guardar_puntos(lista_puntos)

        elif opcion == "3":
            # Acumular puntos (simulación de recompensa)
            print("\n--- Acumular puntos (simulación) ---")
            print("Ejemplos de uso:")
            print("- Viaje o reserva completada.")
            print("- Renta de carro con cierta marca.")
            cantidad_texto = input("¿Cuántos puntos quieres agregar como recompensa?: ").strip()
            try:
                cantidad = int(cantidad_texto)
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            agregar_puntos(id_usuario, cantidad, lista_puntos)
            print("Puntos agregados correctamente.")

            # Actualizamos el registro local y guardamos
            registro = buscar_registro_por_usuario(lista_puntos, id_usuario)
            guardar_puntos(lista_puntos)

        elif opcion == "4":
            print("Volviendo al menú principal...")
        else:

            print("Opción no válida. Intenta de nuevo.")
