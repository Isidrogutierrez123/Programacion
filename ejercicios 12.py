# # Ejercicio 1: Crear y Escribir en un Archivo de Texto


with open('saludo.txt', 'w') as archivo:
    archivo.write("¡Hola, bienvenidos al curso de Python!")





# Ejercicio 2: Leer el Contenido de un Archivo de Texto

with open('saludo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)


# # Ejercicio 3: Escribir Múltiples Líneas en un Archivo

with open('saludo.txt', 'w') as archivo:
    for i in range(3):
        nota = input(f"Ingrese la nota {i + 1}: ")
        archivo.write(nota +'n' )


# # Ejercicio 4: Leer un Archivo Línea por Línea

with open('saludo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())

# # Ejercicio 5


entrada_nueva = input("Ingrese su nueva entrada de saludo: ")
with open('saludo.txt', 'a') as archivo:
    archivo.write(entrada_nueva + '\n')

# Mostrar el contenido completo del archivo
with open('saludo.txt', 'r') as archivo:
    contenido = archivo.read()
    print (contenido)