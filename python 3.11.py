import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 15, 25, 35, 45])


resultado = array1 + array2


print(resultado)



# Ejercicio 2

array_ej2 = np.array([2, 4, 6, 8, 10, 12])
resultado_ej2 = array_ej2 * 3
print("Ejercicio :", resultado_ej2)

# Ejercicio 3

array_ej3 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
promedio_ej3 = np.mean(array_ej3)
print("Ejercicio 3:", promedio_ej3)

# Ejercicio 4
array_ej4 = np.array([1, 3, 5, 7, 9, 11, 13, 15])
resultado_ej4 = array_ej4[array_ej4 > 5]
print("Ejercicio 4:", resultado_ej4)

# Ejercicio 5


array_ej5 = np.array([2, 4, 6, 8, 10])
resultado_ej5 = array_ej5 ** 2
print("Ejercicio 5:", resultado_ej5)



resultado_ej2, promedio_ej3, resultado_ej4, resultado_ej5