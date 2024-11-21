# Función para conectar a la base de datos
import mysql.connector
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="CENTRO_DEPORTIVO"
    )
    return conexion

def menu_actividades():
    while True:
        print("\n=== Gestión de Actividades ===")
        print("1. Crear actividad")
        print("2. Ver actividades")
        print("3. Actualizar actividad")
        print("4. Eliminar actividad")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_actividad()
        elif opcion == '2':
            ver_actividades()
        elif opcion == '3':
            actualizar_actividad()
        elif opcion == '4':
            eliminar_actividad()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
def crear_actividad():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        nombre_actividad = input("Ingrese el nombre de la actividad: ")
        horario = input("Ingrese el horario de la actividad (ejemplo: Lunes y Miércoles 18:00): ")
        duracion = int(input("Ingrese la duración en minutos: "))
        id_entrenador = input("Ingrese el ID del entrenador a cargo: ")

        sql = """
            INSERT INTO actividades (nombre_actividad, horario, duracion, id_entrenador)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre_actividad, horario, duracion, id_entrenador)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Actividad registrada exitosamente.")
    
    except Exception as e:
        print(f"Error al registrar la actividad: {e}")

    finally:
        cursor.close()
        conexion.close()
def ver_actividades():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        sql = """
            SELECT a.id_actividad, a.nombre_actividad, a.horario, a.duracion, e.nombre_entrenador
            FROM actividades a
            LEFT JOIN entrenadores e ON a.id_entrenador = e.id_entrenador
        """
        cursor.execute(sql)
        actividades = cursor.fetchall()

        print("\nID | Actividad | Horario | Duración (min) | Entrenador")
        print("-" * 60)
        for actividad in actividades:
            print(f"{actividad[0]} | {actividad[1]} | {actividad[2]} | {actividad[3]} | {actividad[4]}")

    except Exception as e:
        print(f"Error al mostrar actividades: {e}")

    finally:
        cursor.close()
        conexion.close()

        
def actualizar_actividad():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_actividad = input("Ingrese el ID de la actividad a actualizar: ")
        nombre_actividad = input("Ingrese el nuevo nombre de la actividad: ")
        horario = input("Ingrese el nuevo horario: ")
        duracion = int(input("Ingrese la nueva duración en minutos: "))
        id_entrenador = input("Ingrese el nuevo ID del entrenador: ")

        sql = """
            UPDATE actividades 
            SET nombre_actividad = %s, horario = %s, duracion = %s, id_entrenador = %s 
            WHERE id_actividad = %s
        """
        valores = (nombre_actividad, horario, duracion, id_entrenador, id_actividad)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Actividad actualizada exitosamente.")
    
    except Exception as e:
        print(f"Error al actualizar la actividad: {e}")

    finally:
        cursor.close()
        conexion.close()


def eliminar_actividad():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        id_actividad = input("Ingrese el ID de la actividad a eliminar: ")

        sql = "DELETE FROM actividades WHERE id_actividad = %s"
        cursor.execute(sql, (id_actividad,))
        conexion.commit()
        print("Actividad eliminada exitosamente.")
    
    except Exception as e:
        print(f"Error al eliminar la actividad: {e}")

    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    menu_actividades()