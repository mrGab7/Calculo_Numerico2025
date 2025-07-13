def newton_raphson(f, df, x0, tol, max_iter=1000):
    """
    Encuentra una raíz de la función f usando el método de Newton-Raphson.
    
    Parámetros:
    f (function): Función a resolver.
    df (function): Derivada de la función f.
    x0 (float): Valor inicial.
    tol (float): Tolerancia para el error relativo.
    max_iter (int): Número máximo de iteraciones (opcional).
    
    Retorna:
    float: Aproximación de la raíz.
    int: Número de iteraciones realizadas.
    """
    x_prev = x0
    iteracion = 0
    
    for _ in range(max_iter):
        # Evaluar función y derivada
        f_x = f(x_prev)
        df_x = df(x_prev)
        
        # Verificar si la derivada es cero
        if abs(df_x) < 1e-15:
            raise ValueError("Derivada cero en x = {:.6f}".format(x_prev))
        
        # Calcular nueva aproximación
        x_actual = x_prev - f_x / df_x
        iteracion += 1
        
        # Calcular error relativo (evitando división por cero)
        if abs(x_actual) < 1e-15:
            error_rel = abs(x_actual - x_prev)
        else:
            error_rel = abs((x_actual - x_prev) / x_actual)
        
        # Verificar criterio de parada
        if error_rel < tol:
            return x_actual, iteracion
        
        # Preparar siguiente iteración
        x_prev = x_actual
    
    # Si se alcanza el máximo de iteraciones
    return x_prev, iteracion

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la función a resolver (ejemplo: e^x - 2)
    import math
    def funcion_ejemplo(x):
        return math.exp(x) - 2
    
    # Definir su derivada (e^x)
    def derivada_ejemplo(x):
        return math.exp(x)
    
    # Parámetros del método
    x0 = 1.0  # Valor inicial
    tolerancia = 0.0001  # 0.01% de error
    
    raiz, iteraciones = newton_raphson(funcion_ejemplo, derivada_ejemplo, x0, tolerancia)
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Valor de la función en la raíz: {funcion_ejemplo(raiz)}")