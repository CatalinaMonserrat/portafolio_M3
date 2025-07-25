#Programa para determinar si un numero es positivo, negativo o cero

print("Determinar si un número es positivo, negativo o cero")

while True:
    entrada = input("Ingrese un numero o escribe 'salir' para salir: ")

    if entrada.lower() == "salir":
        print("Gracias por usar el programa")
        break
    try:
        num = float(entrada)
        if num > 0:
            print("El número es positivo\n")
        elif num < 0:
            print("El número es negativo\n")
        else:
            print("El número es cero\n")

    except ValueError:
        print("El dato ingresado no es un número")
