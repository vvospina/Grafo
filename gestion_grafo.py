import mysql.connector 
db= mysql.connector.connect(user='root', password= '',host="localhost", database="grafo")
cursor = db.cursor()


def crear_conexion(ciu1_nombre, ciu2_nombre):
    cursor = db.cursor()
    cursor.callproc('crear_conexion', (ciu1_nombre, ciu2_nombre))
    db.commit()
    cursor.close()
    print(f'Conexión creada entre {ciu1_nombre} y {ciu2_nombre}.')

def leer_conexion(ciu1_nombre, ciu2_nombre):
    cursor = db.cursor('leer_conexion', (ciu1_nombre, ciu2_nombre))
    cursor.fetchall()
    db.commit()
    cursor.close()
    print(f'Conexiones entre {ciu1_nombre} y {ciu2_nombre}.')


def actualizar_conexion(id, nueva_ciudad1, nueva_ciudad2):
    cursor = db.cursor()
    cursor.callproc('actualizar_conexion', (id, nueva_ciudad1, nueva_ciudad2))
    db.commit()
    cursor.close()
    print(f'Conexión con ID {id} actualizada a {nueva_ciudad1} - {nueva_ciudad2}.')

def eliminar_conexion(id):
    cursor = db.cursor()
    cursor.callproc('eliminar_conexion', (id,))
    db.commit()
    cursor.close()
    
    print(f'Conexión con ID {id} eliminada.')


def menu():
    while True:
        print("\n BIENVENIDO A CONEXIONES COLOMBIA:")
        print("1. Crear una conexión")
        print("2. Leer las conexiones")
        print("3. Actualizar una conexión")
        print("4. Eliminar una conexión")
        print("5. Salir")
        
        opcion = input("POR FAVOR SELECCIONE UNA OPCIÓN: ")
        
        if opcion == '1':
            ciu1_nombre = input("Ingrese la ciudad 1: ")
            ciu2_nombre = input("Ingrese la ciudad 2: ")
            crear_conexion(ciu1_nombre, ciu2_nombre)
        elif opcion == '2':
            ciu1_nombre = input("Ingrese el nombre de la ciudad1: ")
            ciu2_nombre = input("Ingrese el nombre de la ciudad2: ")
            leer_conexion()   
        elif opcion == '3':
            id = int(input("Ingrese el ID de la conexión a actualizar: "))
            nueva_ciudad1 = input("Ingrese la nueva ciudad 1: ")
            nueva_ciudad2 = input("Ingrese la nueva ciudad 2: ")
            actualizar_conexion(id, nueva_ciudad1, nueva_ciudad2)
        elif opcion == '4':
            id = int(input("Ingrese el ID de la conexión a eliminar: "))
            eliminar_conexion(id)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()