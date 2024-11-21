

import mysql.connector


# Establecer conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",       # Dirección del servidor (localhost para base de datos local)
    user="root",         # Usuario de la base de datos
    password="curso",  # Contraseña del usuario
    database="SUPERMERCADO"    # Nombre de la base de datos
)


# Verificar si la conexión es exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")



# CRUD para la tabla 'productos'

def crear_producto(nombre, precio, id_categoria):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO productos (nombre, precio, id_categoria) 
    VALUES (?, ?, ?)
    ''', (nombre, precio, id_categoria))
    conn.commit()
    conn.close()

def leer_productos():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()
    return productos

def actualizar_producto(id_producto, nombre, precio, id_categoria):
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE productos SET nombre = ?, precio = ?, id_categoria = ? WHERE id = ?
    ''', (nombre, precio, id_categoria, id_producto))
    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conn.commit()
    conn.close()

# CRUD para la tabla 'categorias'

def leer_categorias():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categorias')
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def menu_principal():
    while True:
        print("\n===== Menú Principal =====")
        print("1. Productos")
        print("2. Categorías")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_categorias()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_productos():
    while True:
        print("\n===== Menú de Productos =====")
        print("1. Crear Producto")
        print("2. Leer Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categorias = leer_categorias()
            print("\nCategorías disponibles:")
            for categoria in categorias:
                print(f"{categoria[0]}. {categoria[1]}")
            id_categoria = int(input("Selecciona una categoría: "))
            crear_producto(nombre, precio, id_categoria)

        elif opcion == "2":
            productos = leer_productos()
            for producto in productos:
                print(f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: {producto[2]} | Categoría ID: {producto[3]}")
        elif opcion == "3":

            id_producto = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre del producto: ")
            precio = float(input("Nuevo precio del producto: "))
            categorias = leer_categorias()

            print("\nCategorías disponibles:")
            for categoria in categorias:
                print(f"{categoria[0]}. {categoria[1]}")
            id_categoria = int(input("Selecciona una categoría: "))
            actualizar_producto(id_producto, nombre, precio, id_categoria)

        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)

        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_categorias():
    while True:
        print("\n===== Menú de Categorías =====")
        print("1. Leer Categorías")
        print("2. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            categorias = leer_categorias()
            for categoria in categorias:
                print(f"ID: {categoria[0]} | Nombre: {categoria[1]}")
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")






if __name__ == "__main__":
    menu_principal()







