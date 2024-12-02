from pymongo import MongoClient
from pedido import Pedido
from cliente import Cliente
import uuid
client = MongoClient('mongodb://localhost:27017/') #reemplaza si es diferente
db = 'comercio_electronico'

cliente = Cliente(client, db)
pedido = Pedido(client, db)

def menu_cliente():
    """Menú para gestionar clientes."""
    while True:
        print("\n--- Menú Clientes ---")
        print("1. Crear Cliente")
        print("2. Leer Todos los Clientes")
        print("3. Leer Cliente por ID")
        print("4. Actualizar Cliente")
        print("5. Eliminar Cliente")
        print("6. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            
            nombre = input("Nombre: ")
            email = input("Email: ")
            fecha_registro = input("Fecha de Registro (YYYY-MM-DD): ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")

            data = {
                "_id": str(uuid.uuid4()), 
                "nombre": nombre,
                "email": email,
                "fecha_registro": fecha_registro,
                "direccion": direccion,
                "telefono": telefono,
            }

            resultado = cliente.create_cliente(data)
            print(f"Cliente creado con ID: {resultado}")

        elif opcion == "2":
            
            print("\n--- Lista de Clientes ---")
            clientes = cliente.read_cliente()
            for c in clientes:
                print(c)

        elif opcion == "3":
            
            cliente_id = input("Ingresa el ID del Cliente: ")
            resultado = cliente.read_cliente_by_id(cliente_id)
            if resultado:
                print("\n--- Cliente Encontrado ---")
                print(resultado)
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            
            cliente_id = input("Ingresa el ID del Cliente a actualizar: ")
            nombre = input("Nuevo Nombre (deja vacío para no cambiar): ")
            email = input("Nuevo Email (deja vacío para no cambiar): ")
            direccion = input("Nueva Dirección (deja vacío para no cambiar): ")
            telefono = input("Nuevo Teléfono (deja vacío para no cambiar): ")

            data = {}
            if nombre: data["nombre"] = nombre
            if email: data["email"] = email
            if direccion: data["direccion"] = direccion
            if telefono: data["telefono"] = telefono

            resultado = cliente.update_cliente(cliente_id, data)
            print(f"Documentos modificados: {resultado}")

        elif opcion == "5":
          
            cliente_id = input("Ingresa el ID del Cliente a eliminar: ")
            resultado = cliente.delete_cliente(cliente_id)
            print(f"Documentos eliminados: {resultado}")

        elif opcion == "6":
            
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def menu_pedido():
    """Menú para gestionar pedidos."""
    while True:
        print("\n--- Menú Pedidos ---")
        print("1. Crear Pedido")
        print("2. Leer Todos los Pedidos")
        print("3. Leer Pedido por ID")
        print("4. Actualizar Pedido")
        print("5. Eliminar Pedido")
        print("6. Volver al Menú Principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            
            cliente_id = input("ID del Cliente: ")
            fecha_pedido = input("Fecha del Pedido (YYYY-MM-DD): ")
            monto_total = float(input("Monto Total: "))
            productos = []
            while True:
                producto_id = input("ID del Producto (deja vacío para terminar): ")
                if not producto_id:
                    break
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                productos.append({"producto_id": producto_id, "cantidad": cantidad, "precio": precio})

            data = {
                "cliente_id": cliente_id,
                "fecha_pedido": fecha_pedido,
                "monto_total": monto_total,
                "productos": productos,
            }

            resultado = pedido.create_pedido(data)
            print(f"Pedido creado con ID: {resultado}")

        elif opcion == "2":
            
            print("\n--- Lista de Pedidos ---")
            pedidos = pedido.read_pedidos()
            for p in pedidos:
                print(p)

        elif opcion == "3":
            
            pedido_id = input("Ingresa el ID del Pedido: ")
            resultado = pedido.read_pedidos_by_id(pedido_id)
            if resultado:
                print("\n--- Pedido Encontrado ---")
                print(resultado)
            else:
                print("Pedido no encontrado.")

        elif opcion == "4":
            
            pedido_id = input("Ingresa el ID del Pedido a actualizar: ")
            fecha_pedido = input("Nueva Fecha del Pedido (deja vacío para no cambiar): ")
            monto_total = input("Nuevo Monto Total (deja vacío para no cambiar): ")

            data = {}
            if fecha_pedido: data["fecha_pedido"] = fecha_pedido
            if monto_total: data["monto_total"] = float(monto_total)

            resultado = pedido.update_pedido(pedido_id, data)
            print(f"Documentos modificados: {resultado}")

        elif opcion == "5":
            
            pedido_id = input("Ingresa el ID del Pedido a eliminar: ")
            resultado = pedido.delete_pedido(pedido_id)
            print(f"Documentos eliminados: {resultado}")

        elif opcion == "6":
            
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def menu_principal():
    """Menú principal de la aplicación."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Clientes")
        print("2. Gestionar Pedidos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_pedido()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()


