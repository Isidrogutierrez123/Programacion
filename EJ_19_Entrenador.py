import mysql.connector
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="CENTRO_DEPORTIVO"
    )
    return conexion


def menu_entrenadores():
    while True:
        print("\n=== Gestión de Entrenadores ===")
        print("1. Crear entrenador")
        print("2. Ver entrenadores")
        print("3. Actualizar entrenador")
        print("4. Eliminar entrenador")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_entrenador()
        elif opcion == '2':
            ver_entrenadores()
        elif opcion == '3':
            actualizar_entrenador()
        elif opcion == '4':
            eliminar_entrenador()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
            

def crear_entrenador():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        nombre_entrenador = input("Ingrese el nombre del entrenador: ")
        especialidad = input("Ingrese la especialidad del entrenador: ")

        sql = "INSERT INTO entrenadores (nombre_entrenador, especialidad) VALUES (%s, %s)"
        valores = (nombre_entrenador, especialidad)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Entrenador registrado exitosamente.")
    
    except Exception as e:
        print(f"Error al registrar el entrenador: {e}")

    finally:
        cursor.close()
        conexion.close()

def ver_entrenadores():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM entrenadores")
        entrenadores = cursor.fetchall()

        print("\nID | Nombre | Especialidad")
        print("-" * 30)
        for entrenador in entrenadores:
            print(f"{entrenador[0]} | {entrenador[1]} | {entrenador[2]}")

    except Exception as e:
        print(f"Error al mostrar entrenadores: {e}")

    finally:
        cursor.close()
        conexion.close()


def actualizar_entrenador():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_entrenador = input("Ingrese el ID del entrenador a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nueva_especialidad = input("Ingrese la nueva especialidad: ")

        sql = """
            UPDATE entrenadores 
            SET nombre_entrenador = %s, especialidad = %s 
            WHERE id_entrenador = %s
        """
        valores = (nuevo_nombre, nueva_especialidad, id_entrenador)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Entrenador actualizado exitosamente.")

    except Exception as e:
        print(f"Error al actualizar el entrenador: {e}")

    finally:
        cursor.close()
        conexion.close()


def eliminar_entrenador():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_entrenador = input("Ingrese el ID del entrenador a eliminar: ")

        sql = "DELETE FROM entrenadores WHERE id_entrenador = %s"
        cursor.execute(sql, (id_entrenador,))
        conexion.commit()
        print("Entrenador eliminado exitosamente.")
    
    except Exception as e:
        print(f"Error al eliminar el entrenador: {e}")

    finally:
        cursor.close()
        conexion.close()



if __name__ == "__main__":
    menu_entrenadores()
