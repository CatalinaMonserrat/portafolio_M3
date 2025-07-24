# Conversor de monedas

print("Bienvenido al Conversor de divisas")

valor_CLP= 1
valor_USD= 957.23
valor_EUR= 1110.81
valor_Yuan=  132.49

def menu ():
    print("1. CLP a Dolares")
    print("2. CLP a Euros")
    print("3. CLP a Yuanes")
    print("4. Dolares a Pesos")
    print("5. Euro a pesos")
    print("6. Yuanes a pesos")
    print("7. Salir")
def convertir (pesos, valor):
    return pesos / valor

def convertir2 (moneda, valor):
    return moneda *valor


while True:
    menu()
    try:
        Valor1 = int(input("Ingrese una opcion deseada: "))
    except ValueError:
        print("Opcion no valida. Intente nuevamente")
        continue

    if (Valor1 == 7):
        print("Gracias por usar el Conversor de divisas")
        break

    elif(Valor1 == 1):
        pesos = float(input("Ingrese los pesos que desea convertir: "))
        dolares = convertir(pesos, valor_USD)
        print(f"Los dolares son: {dolares :.2f}")
    elif (Valor1 == 2):
        pesos = float(input("Ingrese los pesos que desea convertir: "))
        euros = convertir(pesos, valor_EUR)
        print(f"Los euros son: {euros :.2f}")
    elif (Valor1 == 3):
        pesos = float(input("Ingrese los pesos que desea convertir: "))
        yuanes = convertir(pesos, valor_Yuan)
        print(f"Los yuanes son: {yuanes :.2f}")
    elif (Valor1 == 4):
        dolares = float(input("Ingrese los dolares que desea convertir: "))
        pesos = convertir2(dolares, valor_USD)
        print(f"Los pesos son: {pesos :.2f}")
    elif (Valor1 == 5):
        euros = float(input("Ingrese los euros que desea convertir: "))
        pesos = convertir2(euros, valor_EUR)
        print(f"Los pesos son: {pesos :.2f}")
    elif (Valor1 == 6):
        yuanes = float(input("Ingrese los yuanes que desea convertir: "))
        pesos = convertir2(yuanes, valor_Yuan)
        print(f"Los pesos son: {pesos :.2f}")