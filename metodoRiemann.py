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

def pedir_metodo():
    while True:
        metodo = input("Elija el método (izquierda/derecha/medio): ").lower()
        if metodo in ['izquierda', 'derecha', 'medio']:
            return metodo
        print("Método no válido. Por favor elija entre 'izquierda', 'derecha' o 'medio'.")

def calcular_integral_riemann():
    """
    Realiza la estimación de la integral definida de una función utilizando sumas de Riemann
    con una cantidad determinada de subintervalos que el usuario especifica.
    """
    print("\n" + "="*60)
    print("Calculadora de Integrales usando el método de Riemann")
    print("="*60)

    funcion_str = pedir_funcion()
    a = pedir_float("Ingrese el límite inferior de integración (a): ")
    b = pedir_float("Ingrese el límite superior de integración (b): ")
    if b < a:
        print("Se intercambian los límites para que el superior sea mayor.")
        a, b = b, a
    n = pedir_int("Ingrese el número de subintervalos (n): ")
    metodo = pedir_metodo()

    delta_x = (b - a) / n
    suma = 0.0
    valores = []

    for i in range(n):
        if metodo == 'izquierda':
            x_eval = a + i * delta_x
        elif metodo == 'derecha':
            x_eval = a + (i + 1) * delta_x
        else:  # medio
            x_eval = a + (i + 0.5) * delta_x
        try:
            y_i = eval(funcion_str, {'math': math, 'x': x_eval})
            area_rectangulo = y_i * delta_x
            suma += area_rectangulo
            valores.append((x_eval, y_i, area_rectangulo))
        except Exception as e:
            print(f"Error al evaluar la función en x = {x_eval:.6f}: {e}")
            return

    print("\n" + "="*60)
    print("RESULTADO")
    print("="*60)
    print(f"Función: {funcion_str}")
    print(f"Límites: [{a}, {b}]")
    print(f"Método: {'Punto izquierdo' if metodo == 'izquierda' else 'Punto derecho' if metodo == 'derecha' else 'Punto medio'}")
    print(f"Número de subintervalos: {n}")
    print(f"Ancho de cada subintervalo (Δx): {delta_x:.6f}")
    print(f"Suma total (integral aproximada): {suma:.8f}")

    detalle = input("\n¿Desea ver detalles del cálculo? (s/n): ").lower()
    if detalle == 's':
        print("\nDetalles de los rectángulos:")
        print("i |   x_eval   |   f(x_eval)   |   Área del rectángulo")
        print("-" * 60)
        for i, (x_eval, y_i, area) in enumerate(valores):
            print(f"{i+1:2d} | {x_eval:10.6f} | {y_i:13.6f} | {area:18.8f}")

if __name__ == "__main__":
    while True:
        calcular_integral_riemann()
        continuar = input("\n¿Desea calcular otra integral? (s/n): ").lower()
        while continuar not in ['s', 'n']:
            print("Opción no válida. Por favor ingrese 's' o 'n'.")
            continuar = input("¿Desea calcular otra integral? (s/n): ").lower()
        if continuar == 'n':
            print("\n¡Gracias por usar la calculadora de integrales!")
            break