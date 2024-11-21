

# Ejercicio 1: Guardar una Lista de Números en un Archivo y Leerla como un Array


import numpy as np

# Generar un array de 10 números enteros aleatorios entre 1 y 100
numeros = np.random.randint(1, 101, size=10)


with open('numeros.txt', 'w') as f:
    for numero in numeros:
        f.write(f"{numero}\n")


numeros_leidos = np.loadtxt('numeros.txt', dtype=int)

print("Números leídos del archivo:", numeros_leidos)




# Ejercicio 2: Cargar Datos de un Archivo y Calcular Estadísticas


with open('temperaturas.txt', 'w') as f:
    temperaturas = [15, 20, 25, 30, 28, 22, 18, 16, 21, 24, 26, 19]
    for temp in temperaturas:
        f.write(f"{temp}\n")


temperaturas_leidas = np.loadtxt('temperaturas.txt', dtype=float)


promedio = np.mean(temperaturas_leidas)
maxima = np.max(temperaturas_leidas)
minima = np.min(temperaturas_leidas)


print(f"Temperatura promedio: {promedio:.2f}°C")
print(f"Temperatura más alta: {maxima:.2f}°C")
print(f"Temperatura más baja: {minima:.2f}°C")



# Ejercicio 3: Procesar Notas de Estudiantes desde un Archivo


import numpy as np


with open('notas_estudiantes.txt', 'w') as f:
    notas = [
        "85,90,78",
        "88,92,95",
        "70,75,80",
        "60,65,70",
        "95,100,98"
    ]
    for nota in notas:
        f.write(f"{nota}\n")


notas_leidas = np.loadtxt('notas_estudiantes.txt', delimiter=',', dtype=float)

promedios_estudiantes = np.mean(notas_leidas, axis=1)
promedio_clase = np.mean(promedios_estudiantes)


print("Promedio de calificaciones por estudiante:", promedios_estudiantes)
print(f"Promedio general de la clase: {promedio_clase:.2f}")


# Ejercicio 4: Filtrar y Guardar Valores en un Nuevo Archivo

import numpy as np

with open('valores.txt', 'w') as f:
    valores = np.random.randint(-50, 51, size=15)
    for valor in valores:
        f.write(f"{valor}\n")


valores_leidos = np.loadtxt('valores.txt', dtype=int)


valores_positivos = valores_leidos[valores_leidos > 0]


with open('valores_positivos.txt', 'w') as f:
    for valor in valores_positivos:
        f.write(f"{valor}\n")


print("Valores positivos:", valores_positivos)




# Ejercicio 5: Guardar una Matriz en un Archivo y Leerla

import numpy as npA


matriz = np.random.randint(1, 11, size=(3, 3))


with open('matriz.txt', 'w') as f:
    for fila in matriz:
        f.write(','.join(map(str, fila)) + '\n')


matriz_leida = np.loadtxt('matriz.txt', delimiter=',', dtype=int)


print("Matriz leída del archivo:")
print(matriz_leida)