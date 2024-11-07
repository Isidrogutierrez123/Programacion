
import mysql.connector


# Establecer conexión con la base de datos
def conectar():
    return  mysql.connector.connect(
    host="localhost",       # Dirección del servidor (localhost para base de datos local)
    user="root",         # Usuario de la base de datos
    password="Campusfp2425",  # Contraseña del usuario
    database="mercado"    # Nombre de la base de datos
)


# Verificar si la conexión es exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")



def crear_categoria():
    conexion = conectar()
    cursor = conexion.cursor()
    idcategoria = int(input("Ingrese el id que quieras crear:"))


    cursor.execute("Insert INTO")

def leer_categorias():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    print("Listado de Categorías:")
    for categoria in categorias:
        print(f"{categoria[0]} - {categoria[1]}")

def actualizar_categoria():
    idcategoria = int(input("Ingrese el ID de la categoría a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
    cursor.execute("UPDATE categoria SET nombre = ? WHERE idcategoria = ?", (nuevo_nombre, idcategoria))
    if cursor.rowcount == 0:
        print("Error: La categoría no existe.")
    else:
        conn.commit()
        print(f"La categoría con ID {idcategoria} ha sido actualizada a '{nuevo_nombre}'.")

def eliminar_categoria():
    idcategoria = int(input("Ingrese el ID de la categoría que quieres eliminar: "))
    cursor.execute("DELETE FROM categoria WHERE idcategoria = ?", (idcategoria,))
    if cursor.rowcount == 0:
        print("Error: La categoría no existe.")
    else:
        conn.commit()
        print(f"La categoría con ID {idcategoria} ha sido eliminada.")


def mostrar_menu():
    while True:
        print("/nGestióndecategorias")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Salir")


        eleccion_usuario=int(input("Opcion: "))


        if eleccion_usuario == "1":
            crear_categoria()
        if eleccion_usuario == "2":
            leer_categoria()    
        if eleccion_usuario == "3":
            actualizar_categoria()
        if eleccion_usuario == "4":
            eliminar_categoria()

        if eleccion_usuario =="5":
            
            print("Has salido del menu")
            break




