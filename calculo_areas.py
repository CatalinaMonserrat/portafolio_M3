# Calculo de áreas de figuras geometricas

def area_cuadrado(lado):
    """Formula calculo área cuadrado"""
    return lado * lado

def area_rectangulo(base, altura):
    """Formula calculo área rectangulo"""
    return base * altura

def area_triangulo(base, altura):
    """Formula calculo área triangulo"""
    return (base * altura) / 2

def area_circulo(radio):
    """Formula calculo área circulo"""
    return 3.1416 * (radio**2)

def area_trapezio(base_mayor, base_menor, altura):
    """Formula calculo área trapezio"""
    return ((base_mayor + base_menor) * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    """Formula calculo área rombo"""
    return (diagonal_mayor * diagonal_menor) / 2

def area_paralelogramo(base, altura):
    """Formula calculo área paralelogramo"""
    return base * altura

# Menu interactivo

while True:
    print("\n Calculadora de áreas geometrica, elige una figura: \n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo")
    print("5. Trapezio")
    print("6. Rombo")
    print("7. Paralelogramo")
    print("8. Salir")
    print(" \n")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = area_cuadrado(lado)
        print(f"El area del cuadrado es: {round(area, 2)}\n")

    elif opcion == "2":
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = area_rectangulo(base, altura)
        print(f"El area del rectangulo es: {round(area, 2)}")

    elif opcion == "3":
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = area_triangulo(base, altura)
        print(f"El area del triangulo es: {round(area, 2)}")
    
    elif opcion == "4":
        radio = float(input("Ingrese el radio del circulo: "))
        area = area_circulo(radio)
        print(f"El area del circulo es: {round(area, 2)}")

    elif opcion == "5":
        base_mayor = float(input("Ingrese la base mayor del trapezio: "))
        base_menor = float(input("Ingrese la base menor del trapezio: "))
        altura = float(input("Ingrese la altura del trapezio: "))
        area = area_trapezio(base_mayor, base_menor, altura)
        print(f"El area del trapezio es: {round(area, 2)}")   

    elif opcion == "6":
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        area = area_rombo(diagonal_mayor, diagonal_menor)
        print(f"El area del rombo es: {round(area, 2)}")
    
    elif opcion == "7":
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = area_paralelogramo(base, altura)
        print(f"El area del paralelogramo es: {round(area, 2)}")

    elif opcion == "8":
        print("Hasta luego")
        break

    else:
        print("Opcion no valida, intente nuevamente\n")