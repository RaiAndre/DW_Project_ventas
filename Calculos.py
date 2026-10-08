print("Bienvenido al programa de suma de dos números.")
# Solicitar los dos números al usuario
while True:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

# Sumar los números
    suma = num1 + num2

# Mostrar el resultado
    print("La suma es:", suma)
    repetir = input("¿Quieres sumar otros números? (s/n): ").lower()
    if repetir != "s":
        print("¡Hasta luego!")
        break