    # Estructura para almacenar clientes y pedidos
clientes = {} 
pedidos = {}  
productos = {  
    1: {"nombre": "Producto A", "precio": 10.0},
    2: {"nombre": "Producto B", "precio": 15.0},
    3: {"nombre": "Producto C", "precio": 20.0}
}

# Menú principal
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar Cliente")
        print("2. Ver Clientes")
        print("3. Buscar Cliente")
        print("4. Hacer Compra")
        print("5. Seguir Pedido")
        print("6. Salir")
        opcion = input("Elige una opción: ")  #Preguntar la opcion

        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            realizar_compra()
        elif opcion == "5":
            seguimiento_pedido()
        elif opcion == "6":
            print("¡Gracias! Adiós.")
            break  #Final del bucle 
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Si la opción es inválida

# Función para registrar un cliente
def registrar_cliente():
    print("\nRegistrar Cliente")
    identificador = input("ID (por ejemplo, correo): ")  # Pedimos el ID del cliente
    if identificador in clientes:  # Verificamos si el cliente ya está registrado
        print("¡Este cliente ya está registrado!")
    else:
        # Si el cliente no está registrado, pedimos sus datos
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        # Registramos al cliente en el diccionario
        clientes[identificador] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        }
        print("Cliente registrado con éxito.")

# Función para mostrar todos los clientes
def mostrar_clientes():
    print("\nLista de Clientes")
    if not clientes:  # Si no hay clientes registrados
        print("No hay clientes registrados.")
        return
    for id_cliente, datos in clientes.items():  
       
        print(f"{id_cliente}: {datos['nombre']}, {datos['direccion']}, {datos['telefono']}")  # Muestra los datos del cliente

# Buscar un cliente por su Id
def buscar_cliente():
    print("\nBuscar Cliente")
    identificador = input("ID del cliente: ")  
    if identificador in clientes:  # Si el cliente existe en el diccionario
        datos = clientes[identificador]
      
        print(f"Cliente encontrado: {datos['nombre']}, {datos['direccion']}, {datos['telefono']}")   # Muestra los datos del cliente encontrado
    else:
        print("Cliente no encontrado.")  # Si el cliente no existe dar error

# Función para relizar una compra
def realizar_compra():
    print("\nRealizar Compra")
    identificador = input("ID del cliente: ")  
    if identificador not in clientes:  # Comprueba si el cliente esta registrado
        print("¡Cliente no encontrado! Registra al cliente primero.")
        return
    
    print("\nProductos disponibles:")
    for id_producto, info in productos.items():  # Mostramos los productos disponibles
        print(f"{id_producto}: {info['nombre']} - {info['precio']}€")
    
    seleccionados = []  # Lista para almacenar los productos seleccionados por el cliente
    while True:
        try:
            producto_id = int(input("Selecciona un producto (0 para terminar): "))  # Selección de producto
            if producto_id == 0:  # Si ponemos 0 finalizará
                break
            if producto_id in productos:  # Verificamos si el ID es válido
                seleccionados.append(producto_id)  # Añadimos el producto a la lista de seleccionados
            else:
                print("ID de producto inválido.")  # Si el ID no es válido dar error
        except ValueError:
            print("Por favor, ingresa un número válido.")  # Si la entrada no es un número

    if seleccionados:
        numero_pedido = len(pedidos) + 1  # Generamos un número para el pedido
        total = sum(productos[pid]["precio"] for pid in seleccionados)  # Calculamos el total de la compra
        
        pedidos[numero_pedido] = {
            "cliente": identificador,
            "productos": seleccionados,
            "total": total
        }
        print(f"Pedido realizado con éxito. Número de pedido: {numero_pedido}")
        print(f"Total a pagar: {total}€")
    else:
        print("No seleccionaste ningún producto.")  # Si no se seleccionaron productos

# Función para seguir el estado de un pedido
def seguimiento_pedido():
    print("\nSeguir Pedido")
    try:
        numero_pedido = int(input("Número de pedido: "))  
        if numero_pedido in pedidos:  # Si el pedido existe
            pedido = pedidos[numero_pedido]
            cliente_id = pedido["cliente"]
            # Muestra los detalles del pedido
            print(f"Cliente: {clientes[cliente_id]['nombre']}")
            print("Productos en el pedido:")
            for i in pedido["productos"]:
                print(f"- {productos[i]['nombre']} ({productos[i]['precio']}€)")  # Productos comprados
            print(f"Total: {pedido['total']}€")  # Precio total
        else:
            print("Pedido no encontrado.")  # Si el pedido no existe dar error
    except ValueError:
        print("Por favor, ingresa un número válido.") 


# Ejecutar el programa
menu()  
