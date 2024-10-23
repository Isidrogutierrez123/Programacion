#lado = 5
#area = lado + ladoprint("El area del cuadradoes", area) #


#nombre= "Isidro"
#edad= 18
#print("18 es la edad de isidro")


#edad = int(input("Dime tu edad:"))

#if edad >= 18:
       #print("Eres mayor de edad")

#else: 
        #print("Es mayor de edad")



#edad = (input("Dime tu edad:"))

#if edad <= 5:
   # print("Tu entrada es gratuita")
#elif 5 <= edad <= 12:
    #print("Tu entrada cuesta 5€")
#elif 13 <= edad <= 17:
   #print("Tu entrada cuesta 7€")
#else edad >= 18:
   # print("Tu entrada cuesta 10€")



#nota=int(input("Dime tu nota"))

#match nota:

   # case 90:
     #   print("A")
    #case 80:
   #     print("B")
    #case 70:
    #    print("C")
   # case 60:
    #    print("D")
   # case _:
       # print("F")
#
#numero= int(input("Dime un numero correspondientea un dia de la semana"))



#match numero:
   # case 1:
       # print("Lunes")
   # case 2:
       # print("Martes")       
   # case 3:
       # print("Miercoles")
   # case 4:
       # print("Jueves")
   # case 5:
       # print("Viernes")    
   # case 6:
       # print("Sabado")
  #  case 7:
      #  print("Domingo")
  #  case _:
        #print("No valido")


    # Ejercicio 1 Python 01 #


# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# operacion = str(input("Que operacion quieres hacer:"))

# if operacion == "suma":
#     resultadosuma = num1 + num2
#     print("la suma es", resultadosuma)
# elif operacion == "resta":
#     resultadoresta = num1 - num2
#     print("La resta es", resultadoresta)
# elif operacion =="multiplicacion":
#     resultadomulti = num1 * num2
#     print("El resultado es", resultadomulti)

# else:
#     print("No hay mas operaciones")

# if operacion =="division" and num2 == 0:
#     print("Error")
# elif operacion == "division":
#     resultadodivi = num1 / num2
#     print("La multipicacion es", resultadodivi)

    #Ejercicio  2 #

# num= float(input("Ingrese un numero:"))

# if num % 2 == 0:
#         print("El numero es par.")
# else:
#         print("EL numero es impar.")

    #Ejercicio  3 #




# numero = int(input("Ingrese un numero:"))

# suma = 0
# for i in range(1, numero +1) :
#     suma = suma + i
# print("La suma de los numeros es", suma)



#EJERCICIO 5

# num= 20
# adivinar = int(input("Adivina el numero:"))
# while adivinar != num:
#         if adivinar < num:
#             print("No, mas alto")
#         elif adivinar > num:
#             print("No, mas bajo")
#         adivinar = int(input("Adivina el numero:"))

# print("Lo has adivinado lmao")





# lista1 = [1,2,3,4]

# tupla1 = [1,2,3,4]

# print("Valor de la lista")
# print(lista1)

# print("valor de la tupla")
# print(tupla1)

# lista1[0] = 10
# print("Valor de la lista")
# print (lista1)

# tupla1[0]= 10
# print("valor de la tupla")
# print(tupla1)

# dic1 ={}

# nombre = input("Introduce el nombre del nuevo contacto:")
# telefono = input(f"Introduce el telefono de {nombre}:")

# dic1[nombre] = telefono #Insertamos un nuevo par clave en el diccionario

# print("Esta es tu agenda")
# print(dic1)

# print("Vamos a modificar el telefono de un contacto:")
# nombre_busqueda = input("Dame el nombre del contacto que quieres cambiar:")
# telefono_nuevo = input("Dame el nuevo numero de telefono:")

# dic1[nombre_busqueda] = telefono_nuevo




# EJERCICIOS 03 14/10/2024


# #EJERCICIO 3
# itinerario = ("Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao")
# # Mostrar el itinerario completo
# print("Itinerario completo:")
# for ciudad in itinerario:
#     print(ciudad)

# # Permitir al usuario ingresar una posición
# posicion = int(input("Ingresa una posición (1-{}): ".format(len(itinerario))))

# # Validar la posición y mostrar la ciudad correspondiente
# if 1 <= posicion <= len(itinerario):
#     ciudad_visitada = itinerario[posicion - 1]  # Restar 1 para ajustar el índice
#     print("La ciudad que visitarás en la posición {} es: {}".format(posicion, ciudad_visitada))
# else:
#     print("Posición inválida. Por favor, ingresa un número entre 1 y {}.".format(len(itinerario)))

# lista_reproduccion= []
# cancion = input('Dame el nombre de una cancion: ')

# while cancion != 'fin' :
#     lista_reproduccion.append(cancion)
# #     cancion = input('Dame el nombre de una canción: ').lower()

# # while True:
# #     cancion =input('Dame el nombre de una canción: ').lower()
# #     if cancion != 'fin':
# #      lista_reproduccion.append(cancion)

# # else:
    

