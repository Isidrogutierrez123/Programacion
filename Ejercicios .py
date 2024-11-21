# Ejercicio 1

productos = [
    {"nombre": "manzana", "perecedero": True},
    {"nombre": "arroz", "perecedero": False},
    {"nombre": "lechuga", "perecedero": True},
    {"nombre": "lentejas", "perecedero": False},
    {"nombre": "plátano", "perecedero": True},
    {"nombre": "sopa enlatada", "perecedero": False}
]

# Función que determina si un producto es perecedero

def es_perecedero(producto):
    return producto["perecedero"]

# Filtrando productos perecederos

productos_perecederos = list(filter(es_perecedero, productos))

# Escribiendo los productos perecederos

print("Productos perecederos:")
for producto in productos_perecederos:
    print(producto["nombre"])




# Ejercicio 2


# Lista de vehículos con su estado de revisión técnica
vehiculos = [
    {"modelo": "Toyota Corolla", "revision": "aprobada"},
    {"modelo": "Ford Fiesta", "revision": "pendiente"},
    {"modelo": "Honda Civic", "revision": "aprobada"},
    {"modelo": "Chevrolet Spark", "revision": "pendiente"},
    {"modelo": "Nissan Sentra", "revision": "aprobada"}
]

# Función que determina si el vehículo ha pasado la revisión
def ha_pasado_revision(vehiculo):
    return vehiculo["revision"] == "aprobada"

# Filtrando vehículos que han pasado la revisión
vehiculos_aprobados = list(filter(ha_pasado_revision, vehiculos))

# Mostrando los vehículos aprobados
print("Vehículos con revisión técnica aprobada:")
for vehiculo in vehiculos_aprobados:
    print(vehiculo["modelo"])





#Ejercicio 3


# Lista de empleados con su estado laboral
empleados = [
    {"nombre": "Juan Pérez", "estado": "activo"},
    {"nombre": "María López", "estado": "inactivo"},
    {"nombre": "Carlos García", "estado": "activo"},
    {"nombre": "Ana Torres", "estado": "inactivo"},
    {"nombre": "Luis Martínez", "estado": "activo"}
]

# Función que determina si un empleado está activo
def es_activo(empleado):
    return empleado["estado"] == "activo"

# Filtrando empleados activos
empleados_activos = list(filter(es_activo, empleados))

# Imprimiendo los nombres de los empleados activos
print("Empleados activos:")
for empleado in empleados_activos:
    print(empleado["nombre"])


#Ejercicio 4

    # Lista de libros con sus categorías
libros = [
    {"titulo": "Cien años de soledad", "categoria": "novela"},
    {"titulo": "El origen de las especies", "categoria": "ensayo"},
    {"titulo": "Poemas de amor", "categoria": "poesía"},
    {"titulo": "1984", "categoria": "novela"},
    {"titulo": "Historia de la filosofía", "categoria": "ensayo"}
]

# Función que determina si un libro es de la categoría "novela"
def es_novela(libro):
    return libro["categoria"] == "novela"

# Filtrando libros de la categoría "novela"
libros_novela = list(filter(es_novela, libros))

# Mostrando los libros de la categoría "novela"
print("Libros de la categoría 'novela':")
for libro in libros_novela:
    print(libro["titulo"])


    



#Ejercicio 5


tareas = [
    {"descripcion": "Enviar informe", "urgente": True},
    {"descripcion": "Revisar correos", "urgente": False},
    {"descripcion": "Preparar presentación", "urgente": True},
    {"descripcion": "Llamar al cliente", "urgente": False},
    {"descripcion": "Actualizar el proyecto", "urgente": True}
]

# Función que determina si una tarea es urgente
def es_urgente(tarea):
    return tarea["urgente"]

# Filtrando tareas urgentes
tareas_urgentes = list(filter(es_urgente, tareas))

# Imprimiendo las tareas urgentes
print("Tareas urgentes:")
for tarea in tareas_urgentes:
    print(tarea["descripcion"])

