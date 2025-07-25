# Sistema de agenda de contactos

import json

def guardar_agenda():
    """Guarda la agenda en un archivo JSON"""
    with open("agenda.json", "w") as archivo:
        json.dump(agenda, archivo)

def cargar_agenda():
    """Carga la agenda desde un archivo JSON"""
    try:
        with open("agenda.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

agenda = cargar_agenda()

def agregar_contacto():
    """Agrega un contacto a la agenda"""
    nombre = input("Ingrese el nombre del contacto: ").lower()
    telefono = input("Ingrese el teléfono del contacto: ")
    correo = input("Ingrese el correo del contacto: ")

    agenda[nombre] = {
        "telefono": telefono,
        "correo": correo
    }
    guardar_agenda()
    print(f"✅ Contacto '{nombre}' agregado exitosamente.\n")

def ver_contacto():
    """Permite ver un contacto en la agenda"""
    if not agenda:
        print("La agenda esta vacia\n")
    else:
        for contacto in agenda:
            print(f"\nContacto: {contacto}")
            print(f"Telefono: {agenda[contacto]['telefono']}")
            print(f"Correo: {agenda[contacto]['correo']}\n")

def buscar_contacto():
    """Busca un contacto en la agenda"""
    nombre = (input("Ingrese el nombre del contacto: ")).lower()
    if nombre in agenda:
        print(f"El telefono de {nombre} es {agenda[nombre]['telefono']}")
        print(f"El correo de {nombre} es {agenda[nombre]['correo']}")
    else:
        print("El contacto no existe\n")

def eliminar_contacto():
    """Elimina un contacto desde la agenda"""
    nombre = input("Ingrese el nombre del contacto a eliminar: ").lower()
    if nombre in agenda:
        del agenda[nombre]
        guardar_agenda()
        print("Contacto eliminado")
    else:
        print("El contacto no existe\n")

# Menu 
while True:
    print("\n Menu: \n")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_contacto()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida, intente nuevamente\n")