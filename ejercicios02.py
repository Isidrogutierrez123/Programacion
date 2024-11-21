


# Ejercicio 1

# palabra = input("Introduce una palabra: ")


# palabra_invertida = ""
# for letra in palabra[::-1]:  
#     palabra_invertida += letra


# print("La palabra invertida es:", palabra_invertida)




# Ejercicio 2

# suma = 0
# contador = 0


# while True:
#     numero = int(input("Introduce un número (0 para terminar): "))
    
#     if numero == 0:
#         break  
    
#     suma += numero
#     contador += 1

# if contador > 0:
#     promedio = suma / contador
#     print("El promedio de los números introducidos es", promedio)
# else:
#     print("No se introdujeron números.")




# Ejercicio 3

# nombres = []


# while True:
#     nombre = input("Introduce un nombre (escribe 'fin' para terminar): ")
    
#     if nombre.lower() == "fin":
#         break 
    
#     nombres.append(nombre)  


# print("Los nombres ingresados son:", nombres)


# print("Lista de nombres:")
# for nombre in nombres:
#     print("-", nombre)



# Ejercicio 4: Verificación de contraseña
# Copiar

# contraseña_correcta = "python123"


# while True:
#     contraseña = input("Introduce la contraseña: ")
    
#     if contraseña == contraseña_correcta:
#         print("¡Acceso concedido!")
#         break  
#     else:
#         print("Contraseña incorrecta, intenta de nuevo.")


# Ejercicio 5: Encontrar el número mayor en una lista
# Copiar

# numeros = []

# while True:
#     entrada = input("Introduce un número (escribe 'hecho' para terminar): ")
    
#     if entrada.lower() == "hecho":
#         break  
    
#     try:
#         numero = float(entrada)  
#         numeros.append(numero)  
#     except ValueError:
#         print("Por favor, introduce un número válido.")


# if numeros:
#     numero_mayor = max(numeros)
#     print("El número mayor ingresado es", numero_mayor)
# else:
#     print("No se introdujeron números.")



