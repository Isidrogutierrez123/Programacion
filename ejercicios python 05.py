# Ejercicio 1

def sumar_cinco(numero):
    return numero + 5

numeros = [1, 2, 3, 4, 5]
resultado = list(map(sumar_cinco, numeros))
print(resultado) 

# Ejercicio 2: 

frases = ["hola mundo", "python es genial", "programar es divertido"]
resultado = list(map(str.title, frases))
print(resultado)  

# Ejercicio 3

def calcular_doble(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]
resultado = list(map(calcular_doble, numeros))
print(resultado)  

# Ejercicio 4

numeros_decimales = [1.1, 2.5, 3.7, 4.3, 5.9]
resultado = list(map(round, numeros_decimales))
print(resultado) 

# Ejercicio 5

def calcular_longitud(palabra):
    return len(palabra)

palabras = ["hola", "mundo", "python", "programar"]
resultado = list(map(calcular_longitud, palabras))
print(resultado)  