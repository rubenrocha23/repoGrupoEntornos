def pedir_numeros():
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor ingresa números válidos.")


def mostrar_menu():
    print("\n" + "="*40)
    print("        CALCULADORA")
    print("="*40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("="*40)