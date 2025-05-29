# Método de Newton-Raphson - Ejemplo con falla cuando la derivada tiende a infinito

def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson
    Parámetros:
    f: función a evaluar
    df: derivada de la función
    x0: valor inicial
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    iteracion = 0
    resultados = []
    x_ant = x0

    while iteracion < max_iter:
        f_x = f(x_ant)
        df_x = df(x_ant)

        # Verificar si la derivada es cercana a cero (o muy inestable)
        if abs(df_x) < 1e-10:
            print(f"\nError: Derivada cercana a cero en la iteración {iteracion + 1}")
            return None

        x = x_ant - f_x / df_x
        error = abs((x - x_ant) / x) * 100 if x != 0 else abs(x - x_ant)

        resultados.append({
            'iteracion': iteracion + 1,
            'x_n': x_ant,
            'f(x_n)': f_x,
            'f\'(x_n)': df_x,
            'x_n+1': x,
            'error': error
        })

        if abs(x - x_ant) < tolerancia:
            break

        x_ant = x
        iteracion += 1

    return resultados

# Caso de prueba que falla: f(x) = x^(1/3), cuya derivada es infinita en x = 0
def f(x):
    return x**(1/3)

def df(x):
    return (1/3) * x**(-2/3)

# Prueba con un valor inicial donde falla
x0 = 0.0
resultados = newton_raphson(f, df, x0)

# Output esperado
"""
Error: Derivada cercana a cero en la iteración 1
"""

# ¿Por qué falla?
# En este ejemplo, la función f(x) = x^(1/3) tiene una derivada f'(x) = (1/3)x^(-2/3),
# la cual no está definida en x = 0, ya que se genera una división entre cero.
# Esto hace que el método de Newton-Raphson no pueda continuar desde ese punto
# y se detiene al detectar que la derivada es demasiado cercana a cero.

# Conclusión:
# Newton-Raphson falla cuando el punto inicial se elige en una zona donde la derivada
# de la función es muy pequeña, infinita o indefinida. En estos casos, el método se vuelve
# inestable y no puede realizar los cálculos correctamente.

