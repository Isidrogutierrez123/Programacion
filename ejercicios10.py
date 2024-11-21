# Ejercicio 1: Crear una Matriz de Ceros y Cambiar Valores

import numpy as np

# Crear una matriz de 3x3 llena de ceros
matriz = np.zeros((3, 3))

matriz[1, 1] = 1

print(matriz)


# Ejercicio 2: Sumar dos Matrices

import numpy as np

# Crear dos matrices de 2x3
matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[7, 8, 9], [10, 11, 12]])

resultado = matriz1 + matriz2

print(resultado)


# Ejercicio 3: Extraer una Columna de una Matriz

import numpy as np

# Crear una matriz de 4x4 con números enteros consecutivos
matriz = np.arange(1, 17).reshape((4, 4))


tercera_columna = matriz[:, 2]
print(tercera_columna)


# Ejercicio 4: Calcular el Promedio de Cada Fila

import numpy as np

# Crear una matriz de 3x4
matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

promedios = np.mean(matriz, axis=1)
print(promedios)


# Ejercicio 5: Encontrar el Valor Máximo en Cada Columna

import numpy as np

# Crear una matriz de 4x3 con valores enteros aleatorios entre 1 y 50
matriz = np.random.randint(1, 51, size=(4, 3))


maximos = np.max(matriz, axis=0)
print(maximos)