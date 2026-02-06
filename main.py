from operaciones.operaciones_basicas import sumar, restar
from operaciones.operaciones_avanzadas import multiplicar, dividir
from operaciones.utilidades import pedir_numeros, mostrar_menu

# operaciones_avanzadas.py

def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        num1, num2 = pedir_numeros()

        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
