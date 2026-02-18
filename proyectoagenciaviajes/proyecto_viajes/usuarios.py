# usuarios.py
# Módulo para registrar usuarios (hasta más de 10000, limitado solo por el archivo).
# Usa un archivo de texto para guardar la información de los usuarios.

ARCHIVO_USUARIOS = "usuarios.txt"


def leer_usuarios(ruta_archivo_usuarios=ARCHIVO_USUARIOS):
    """
    Lee el archivo de usuarios y devuelve una lista de diccionarios.
    Formato de cada línea:
    id_usuario,nombre,email,telefono
    """
    lista_de_usuarios = []

    try:
        archivo = open(ruta_archivo_usuarios, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea == "" or linea.startswith("#"):
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            id_usuario = partes[0]
            nombre = partes[1]
            email = partes[2]
            telefono = partes[3]

            usuario = {
                "id_usuario": id_usuario,
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            lista_de_usuarios.append(usuario)

        archivo.close()
    except FileNotFoundError:
        # Si no existe el archivo, devolvemos lista vacía
        print("Aviso: No se encontró el archivo de usuarios:", ruta_archivo_usuarios)
    except Exception as error:
        print("Error al leer el archivo de usuarios:", error)

    return lista_de_usuarios


def guardar_usuario_en_archivo(usuario, ruta_archivo_usuarios=ARCHIVO_USUARIOS):
    """
    Agrega un usuario al final del archivo de usuarios.
    Formato:
    id_usuario,nombre,email,telefono
    """
    try:
        archivo = open(ruta_archivo_usuarios, "a", encoding="utf-8")
        linea = (
            usuario["id_usuario"] + "," +
            usuario["nombre"] + "," +
            usuario["email"] + "," +
            usuario["telefono"]
        )
        archivo.write(linea + "\n")
        archivo.close()
    except Exception as error:
        print("Error al guardar el usuario en el archivo:", error)


def generar_nuevo_usuario_en_memoria(lista_de_usuarios, nombre, email, telefono):
    """
    Crea un nuevo usuario y lo añade a la lista de usuarios.
    Calcula un nuevo id_usuario numérico incremental.
    Devuelve el usuario creado.
    """
    max_id = 0
    for usuario in lista_de_usuarios:
        try:
            valor = int(usuario["id_usuario"])
            if valor > max_id:
                max_id = valor
        except ValueError:
            continue

    nuevo_id = max_id + 1
    id_usuario_texto = str(nuevo_id)

    nuevo_usuario = {
        "id_usuario": id_usuario_texto,
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    }

    lista_de_usuarios.append(nuevo_usuario)

    return nuevo_usuario


def buscar_usuario_por_id(lista_de_usuarios, id_usuario_buscar):
    """
    Busca un usuario en la lista por su id_usuario.
    Devuelve el diccionario del usuario o None si no existe.
    """
    for usuario in lista_de_usuarios:
        if usuario["id_usuario"] == id_usuario_buscar:
            return usuario
    return None