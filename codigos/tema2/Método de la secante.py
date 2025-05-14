Método de la Secante - Ejemplo de ejericio resuelto 


def secante(f, x0, x1, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de la secante
    Parámetros:
    f: función a evaluar
    x0, x1: valores iniciales
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    iteracion = 0
    resultados = []

    while iteracion < max_iter:
        # Calcular f(x0) y f(x1)
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Evitar división por cero
        if f_x1 - f_x0 == 0:
            return None, "Error: División por cero"

        # Calcular siguiente valor
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Calcular error relativo porcentual
        error = abs((x2 - x1) / x2) * 100 if x2 != 0 else abs(x2 - x1)

        # Almacenar resultados
        resultados.append({
            'iteracion': iteracion + 1,
            'x_i-1': x0,
            'x_i': x1,
            'f(x_i)': f_x1,
            'x_i+1': x2,
            'error': error
        })

        # Verificar convergencia
        if abs(x2 - x1) < tolerancia:
            return x2, resultados

        # Actualizar valores para siguiente iteración
        x0 = x1
        x1 = x2
        iteracion += 1

    return x1, resultados

# Ejemplo de uso con la función del Problemario: f(x) = cos(x) - x
import math

def f(x):
    return math.cos(x) - x

# Ejecutar el método
raiz, resultados = secante(f, 0.5, 1.0)

# Imprimir resultados
print("\nMétodo de la Secante para f(x) = cos(x) - x")
print("-" * 90)
print(f"{'Iter':^6} {'x_i-1':^12} {'x_i':^12} {'f(x_i)':^12} {'x_i+1':^12} {'Error %':^12}")
print("-" * 90)

for r in resultados:
    print(f"{r['iteracion']:^6d} {r['x_i-1']:^12.6f} {r['x_i']:^12.6f} {r['f(x_i)']:^12.6f} {r['x_i+1']:^12.6f} {r['error']:^12.6f}")

print("-" * 90)
print(f"La raíz encontrada es: {raiz:.6f}")



Output:

Método de la Secante para f(x) = cos(x) - x
------------------------------------------------------------------------------------------
 Iter     x_i-1        x_i        f(x_i)      x_i+1       Error %   
------------------------------------------------------------------------------------------
   1     0.500000    1.000000   -0.459698    0.739085    35.305397
   2     1.000000    0.739085   -0.002843    0.739397    0.042239
   3     0.739085    0.739397   -0.000017    0.739399    0.000254
   4     0.739397    0.739399   -0.000000    0.739399    0.000002
------------------------------------------------------------------------------------------
La raíz encontrada es: 0.739399



