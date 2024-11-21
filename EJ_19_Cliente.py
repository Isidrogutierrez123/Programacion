import mysql.connector
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="CENTRO_DEPORTIVO"
    )
    return conexion

def menu_clientes():
    while True:
        print("\n=== Gestión de Clientes ===")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

def crear_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del cliente: ")
    edad = input("Ingrese la edad: ")
    membresia = input("Ingrese el tipo de membresía: ")

    sql = "INSERT INTO clientes (nombre, edad, tipo_membresia) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, edad, membresia))
    conexion.commit()
    print("Cliente registrado exitosamente.")
    conexion.close()

def ver_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        print(cliente)
    conexion.close()


def actualizar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_cliente = input("Ingrese el ID del cliente a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nueva_edad = int(input("Ingrese la nueva edad: "))  # Convertir a entero
        nueva_membresia = input("Ingrese el nuevo tipo de membresía: ")

        # Consulta SQL
        sql = "UPDATE clientes SET nombre = %s, edad = %s, tipo_membresia = %s WHERE id_cliente = %s"
        valores = (nuevo_nombre, nueva_edad, nueva_membresia, id_cliente)

        # Ejecución de la consulta
        cursor.execute(sql, valores)

        # Confirmar cambios
        conexion.commit()
        print("Cliente actualizado exitosamente.")

    except Exception as e:
        print(f"Error al actualizar el cliente: {e}")

    finally:
        cursor.close()
        conexion.close()

def eliminar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        # Solicitar el ID del cliente a eliminar
        id_cliente = input("Ingrese el ID del cliente a eliminar: ")

        # Verificar si el cliente existe
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()

        if cliente:
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de que desea eliminar al cliente '{cliente[1]}'? (s/n): ")
            if confirmacion.lower() == 's':
                # Eliminar cliente
                sql = "DELETE FROM clientes WHERE id_cliente = %s"
                cursor.execute(sql, (id_cliente,))
                conexion.commit()
                print("Cliente eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Cliente no encontrado.")

    except Exception as e:
        print(f"Error al eliminar el cliente: {e}")

    finally:
        cursor.close()
        conexion.close()

        
if __name__ == "__main__":
    menu_clientes()