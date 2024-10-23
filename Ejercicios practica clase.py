#PAra que un numero sea primo tiene que ser mayor que 1, y ser divisible por 1 y por el mismo únicamente, si se divide por cualquier otro número el resto será mayor que 0
# def es_primo(numero):
#     if numero > 1:
#         if numero % numero+1 == 0:
#             print('No es primo')
#         elif (numero % 1 == 0) and (numero % numero == 0):
#             print('Es primo')
#     else:
#         print ('Menor que 1, el número no puede ser primo')


##Programa principal empieza aqui
# numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

# es_primo(numero)

# ##############################################
# #Solucion con return en la funcion es_primo
# ############################################
# def es_primo(numero):
#     valor_devuelto = False
#     if numero > 1:
#         if numero % numero+1 == 0:
#             valor_devuelto = False
#         elif (numero % 1 == 0) and (numero % numero == 0):
#             valor_devuelto = True
#     else:
#         valor_devuelto = False
#     return valor_devuelto

# ##Programa principal empieza aqui
# numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

# valor_funcion = es_primo(numero)

# if valor_funcion == True:
#     print('Es primo')
# else:
#     print('No es primo')