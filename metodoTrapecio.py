import math

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingrese un número válido.")

def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("El número debe ser positivo.")
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def pedir_funcion():
    while True:
        try:
            funcion_str = input("Ingrese la función a integrar (use 'x' como variable, ej: x**2 + math.sin(x)): ")
            x = 1
            eval(funcion_str, {'math': math, 'x': x})
            return funcion_str
        except Exception as e:
            print(f"Error en la función ingresada: {e}. Intente nuevamente.")

def calcular_integral_trapecio():
    """
    Calcula la integral definida de una función usando el método del trapecio
    con un número de subintervalos especificado por el usuario.
    """
    print("\n" + "="*60)
    print("Calculadora de Integrales usando el método del trapecio")
    print("="*60)

    funcion_str = pedir_funcion()
    a = pedir_float("Ingrese el límite inferior de integración (a): ")
    b = pedir_float("Ingrese el límite superior de integración (b): ")
    if b < a:
        print("Se intercambian los límites para que el superior sea mayor.")
        a, b = b, a
    n = pedir_int("Ingrese el número de subintervalos (n): ")

    delta_x = (b - a) / n
    suma = 0.0
    valores = []

    try:
        x0 = a
        xn = b
        y0 = eval(funcion_str, {'math': math, 'x': x0})
        yn = eval(funcion_str, {'math': math, 'x': xn})
        suma = (y0 + yn) / 2.0
        for i in range(1, n):
            xi = a + i * delta_x
            yi = eval(funcion_str, {'math': math, 'x': xi})
            suma += yi
            valores.append((xi, yi))
        integral = suma * delta_x
    except Exception as e:
        print(f"Error al evaluar la función: {e}")
        return

    print("\n" + "="*60)
    print("RESULTADO")
    print("="*60)
    print(f"Función: {funcion_str}")
    print(f"Límites: [{a}, {b}]")
    print(f"Número de subintervalos: {n}")
    print(f"Ancho de cada subintervalo (Δx): {delta_x:.6f}")
    print(f"Integral aproximada: {integral:.8f}")

    detalle = input("\n¿Desea ver detalles del cálculo? (s/n): ").lower()
    if detalle == 's':
        print("\nDetalles de los puntos:")
        print("i |   x_i   |   f(x_i)")
        print("-" * 30)
        print(f"0 | {x0:8.6f} | {y0:10.6f}")
        for i, (xi, yi) in enumerate(valores, start=1):
            print(f"{i} | {xi:8.6f} | {yi:10.6f}")
        print(f"{n} | {xn:8.6f} | {yn:10.6f}")

if __name__ == "__main__":
    while True:
        calcular_integral_trapecio()
        continuar = input("\n¿Desea calcular otra integral? (s/n): ").lower()
        while continuar not in ['s', 'n']:
            print("Opción no válida. Por favor ingrese 's' o 'n'.")
            continuar = input("¿Desea calcular otra integral? (s/n): ").lower()
        if continuar == 'n':
            print("\n¡Gracias por usar la calculadora de integrales!")
            break
