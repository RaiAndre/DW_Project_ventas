import sys

def pedir_numero(mensaje):
    """Pide un número al usuario y valida que sea válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return float(entrada)
        except ValueError:
            print("⚠️  Eso no es un número válido. Intenta de nuevo.")

def pedir_operacion():
    """Pide la operación y valida que sea una de las permitidas."""
    print("\nOperaciones disponibles:")
    print("  1. Suma (+)")
    print("  2. Resta (-)")
    print("  3. Multiplicación (*)")
    print("  4. División (/)")

    while True:
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion in ("1", "2", "3", "4"):
            return opcion
        print("⚠️  Opción no válida. Escribe un número del 1 al 4.")

def calcular(a, b, operacion):
    """Realiza la operación y devuelve el resultado."""
    if operacion == "1":
        return a + b, f"{a} + {b}"
    elif operacion == "2":
        return a - b, f"{a} - {b}"
    elif operacion == "3":
        return a * b, f"{a} × {b}"
    elif operacion == "4":
        if b == 0:
            return None, "división entre cero"
        return a / b, f"{a} ÷ {b}"

def main():
    print("=" * 40)
    print("   CALCULADORA BÁSICA")
    print("=" * 40)

    while True:
        # 1. Pedir la operación
        operacion = pedir_operacion()

        # 2. Pedir los números
        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

        # 3. Calcular
        resultado, expresion = calcular(a, b, operacion)

        # 4. Mostrar resultado
        if resultado is None:
            print(f"\n❌ Error: no se puede hacer una {expresion}.")
        else:
            print(f"\n✅ Resultado: {expresion} = {resultado}")

        # 5. Preguntar si quiere repetir
        while True:
            repetir = input("\n¿Quieres hacer otra operación? (s/n): ").strip().lower()
            if repetir in ("s", "si", "sí", "y", "yes"):
                break
            elif repetir in ("n", "no"):
                print("\n¡Hasta luego! 👋")
                sys.exit()
            else:
                print("⚠️  Respuesta no válida. Escribe 's' o 'n'.")

if __name__ == "__main__":
    main()