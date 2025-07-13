def biseccion(f, a, b, tol, max_iter=1000):
    """
    Encuentra una raíz de la función f en el intervalo [a, b] usando el método de bisección.
    
    Parámetros:
    f (function): Función continua.
    a (float): Extremo izquierdo del intervalo.
    b (float): Extremo derecho del intervalo.
    tol (float): Tolerancia para el error relativo (en decimal, ej. 0.001 para 0.1%).
    max_iter (int): Número máximo de iteraciones (opcional).
    
    Retorna:
    float: Aproximación de la raíz.
    int: Número de iteraciones realizadas.
    """
    if f(a) * f(b) > 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b]")
    
    iteracion = 0
    c_prev = a  # Inicialización para evitar errores en la primera iteración
    
    while iteracion < max_iter:
        c = (a + b) / 2.0
        fa = f(a)
        fc = f(c)
        
        # Comprobar si se encontró la raíz exacta
        if fc == 0.0:
            return c, iteracion + 1
        
        # Actualizar intervalo
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        # Calcular error relativo (después de la primera iteración)
        if iteracion > 0:
            error_rel = abs((c - c_prev) / c)
            if error_rel < tol:
                return c, iteracion + 1
        
        c_prev = c
        iteracion += 1
    
    # Si se alcanza el máximo de iteraciones
    return c, iteracion

# Ejemplo de uso:
if __name__ == "__main__":
    # Definir la función a resolver (ejemplo: e^x - 2)
    import math
    def funcion_ejemplo(x):
        return math.exp(x) - 2
    
    # Parámetros del método
    a = 0.0
    b = 2.0
    tolerancia = 0.0001  # 0.01% de error
    
    raiz, iteraciones = biseccion(funcion_ejemplo, a, b, tolerancia)
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Valor de la función en la raíz: {funcion_ejemplo(raiz)}")