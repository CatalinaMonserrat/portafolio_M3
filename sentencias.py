# Calculadora de Factoriales

print("Bienvenido a la Calculadora de Factoriales interactiva")

nombre = input ("¿Cómo te llamas?")
print(f"Bienvenido {nombre}, vamos a comenzar")

#Definir la Función
def factorial(n):
    """Calcula el factorial de un número"""
    resultado_factorial = 1
    for i in range(1, n + 1):
        resultado_factorial *= i
    return resultado_factorial

while True:
    while True:
        try:
            num = int(input("Ingrese un numero entero positivo: "))
            if num < 0:
                print("El número debe ser positivo")
                continue
            break
        except ValueError:
            print("El dato ingresado no es un número")

    resultado = factorial(num)

    #Mostrar el paso a paso 
    mostrar = input("¿Desea ver el paso a paso? (s/n): ").lower()
    if mostrar == "s":
        for i in range(1, num + 1):
            print(f"{i}! = {factorial(i)}")
    else:
        print(f"\nEl factorial de {num} es {resultado}")

    repetir = input("¿Quieres calcular otro factorial? (s/n): ").lower()
    if repetir != "s":
        break

print(f"\nGracias {nombre}, por usar la Calculadora de Factoriales interactiva")


