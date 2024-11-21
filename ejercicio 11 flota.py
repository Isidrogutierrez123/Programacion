
import numpy as np
import random

# Crear el tablero de 5x5
tablero = np.zeros((5, 5), dtype=int)

# Colocar el barco en una posición aleatoria
fila_barco = random.randint(0, 4)
columna_barco = random.randint(0, 4)
tablero[fila_barco, columna_barco] = 1  # Marca la posición del barco


intentos = 0


def mostrar_tablero(tablero):
    print("Estado del tablero:")
    print(tablero)


while True:
   
    mostrar_tablero(tablero)

    # Pedir al usuario que ingrese las coordenadas de ataque
    try:
        fila = int(input("Ingresa la fila (0-4): "))
        columna = int(input("Ingresa la columna (0-4): "))
        
        
        if fila < 0 or fila > 4 or columna < 0 or columna > 4:
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue
        
       
        intentos += 1

        #
        if tablero[fila, columna] == 1:
            print("¡Has hundido el barco!")
            mostrar_tablero(tablero)
            break
        elif tablero[fila, columna] == -1:
            print("Ya has atacado esta posición. Intenta otra vez.")
        else:
            print("Agua")
            tablero[fila, columna] = -1  

    except ValueError:
        print("Por favor, ingresa números válidos.")

# Mostrar el número total de intentos
print(f"Total de intentos: {intentos}")


