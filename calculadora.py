# calculadora.py
# Versión 2.0: Con bucle y manejo de errores

print("--- CALCULADORA MEJORADA ---")
print("Escribe 'salir' en la operación para terminar.\n")

while True:
    # 1. Pedimos la operación primero para saber si quiere salir
    operacion = input("Operación (+, -, *, /) o 'salir': ").lower()

    if operacion == 'salir':
        print("¡Hasta luego!")
        break # Rompe el ciclo y termina el programa

    # Verificamos si la operación es válida antes de pedir números
    if operacion not in ['+', '-', '*', '/']:
        print("Error: Operación no válida. Intenta de nuevo.")
        continue # Vuelve al inicio del ciclo

    # 2. Bloque protegido contra errores de escritura
    try:
        numero_1 = float(input("Primer número: "))
        numero_2 = float(input("Segundo número: "))
    except ValueError:
        print("Error: Debes ingresar NUMEROS, no letras.")
        continue # Vuelve al inicio

    # 3. Lógica de cálculo
    if operacion == '+':
        print(f"Resultado: {numero_1 + numero_2}")
    elif operacion == '-':
        print(f"Resultado: {numero_1 - numero_2}")
    elif operacion == '*':
        print(f"Resultado: {numero_1 * numero_2}")
    elif operacion == '/':
        if numero_2 != 0:
            print(f"Resultado: {numero_1 / numero_2}")
        else:
            print("Error: No se puede dividir por cero.")
    
    print("-" * 20) # Línea separadora visual