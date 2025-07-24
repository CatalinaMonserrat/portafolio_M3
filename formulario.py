#formulario en consola que solicite información del usuario y la almacene en variables adecuadas.

print("Bienvenido al formulario de registro\n")
print("Por favor, ingrese los siguientes datos:")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese sus apellidos: ")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break #salgo del bucle si ingresa edad correctamente
    except ValueError:
        print("Edad no valida. Intente nuevamente")

while True:
    try:
        estatura = float(input("Ingrese su estatura: "))
        break #salgo del bucle si ingresa estatura correctamente
    except ValueError:
        print("Ingrese su estatuta en metros (1.80). Intente nuevamente")

while True:
    try:
        peso = float(input("Ingrese su peso: "))
        break #salgo del bucle si ingresa peso correctamente
    except ValueError:
        print("Ingrese su peso en kilogramos incluyendo decimales (80.0). Intente nuevamente")

while True:
    respuesta = input("¿Realiza actividad fisica? s/n): ").lower()

    if respuesta == "s":
        tieneEjercicio = True
        break
    elif respuesta == "n":
        desea = input("Desea realizar actividad fisica? s/n): ").lower()
        if desea == "s":
            tieneEjercicio = True
            break
        else:
            tieneEjercicio = False
            print("Gracias por registrarse, su informacion ha sido guardada.")
            exit() #Termina el programas
    else:
        print("Por favor responda con 's' o 'n'. Intente nuevamente")
        
while True:
    respuesta = input("¿Desea ser contactado por un entrenador? s/n): ").lower()

    if respuesta == "s":
        deseaContacto = True
        break
    elif respuesta == "n":
        print("Gracias por registrarse, su informacion ha sido guardada.")
        exit() #Termina el programa
    else:
        print("Por favor responda con 's' o 'n'. Intente nuevamente")

print("Por favor, ingrese los siguientes datos:")
telefono = input("Ingrese su telefono: ")
correo = input("Ingrese su correo: ")

print("\nLos datos ingresados son:")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estatura: {estatura}")
print(f"Peso: {peso}")
print(f"Realiza actividad fisica: {tieneEjercicio}")
print(f"Desea ser contactado por un entrenador: {deseaContacto}")
print(f"Telefono: {telefono}")
print(f"Correo: {correo}")

while True:
    correctos = input("Los datos ingresados son correctos? s/n): ").lower()
    
    if correctos == "s":
        break
    elif correctos == "n":
        print("Vamos a reiniciar el formulario")
        exit() #Termina el programa
    else:
        print("Por favor responda con 's' o 'n'. Intente nuevamente")

print("Gracias por registrarse, su informacion ha sido guardada.")
