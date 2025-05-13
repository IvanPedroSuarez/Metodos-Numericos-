# Método de Punto Fijo
def punto_fijo(g, x0, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de punto fijo
    Parámetros:
    g: función de iteración
    x0: valor inicial
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    iteracion = 0
    resultados = []
    x_ant = x0

    while iteracion < max_iter:
        # Calcular siguiente valor
        x = g(x_ant)

        # Calcular error relativo porcentual
        error = abs((x - x_ant) / x) * 100 if x != 0 else abs(x - x_ant)

        # Almacenar resultados
        resultados.append({
            'iteracion': iteracion + 1,
            'x_n': x_ant,
            'g(x_n)': x,
            'error': error
        })

        # Verificar convergencia
        if abs(x - x_ant) < tolerancia:
            return x, resultados

        x_ant = x
        iteracion += 1

    return x, resultados

# Ejemplo de uso con la función del PDF: e^(-x) = x
# Despejada como g(x) = e^(-x)
import math

def g(x):
    return math.exp(-x)

# Ejecutar el método
raiz, resultados = punto_fijo(g, 0.5)

# Imprimir resultados
print("\nMétodo de Punto Fijo para x = e^(-x)")
print("-" * 60)
print(f"{'Iter':^6} {'x_n':^12} {'g(x_n)':^12} {'Error %':^12}")
print("-" * 60)

for r in resultados:
    print(f"{r['iteracion']:^6d} {r['x_n']:^12.6f} {r['g(x_n)']:^12.6f} {r['error']:^12.6f}")

print("-" * 60)
print(f"La raíz encontrada es: {raiz:.6f}")


Ejecucion:

Método de Punto Fijo para x = e^(-x)
------------------------------------------------------------
 Iter      x_n        g(x_n)      Error %   
------------------------------------------------------------
   1     0.500000    0.606531    17.564392
   2     0.606531    0.545239    11.241755
   3     0.545239    0.579343    5.887923
   4     0.579343    0.560279    3.402833
   5     0.560279    0.571221    1.916843
   6     0.571221    0.564947    1.110955
   7     0.564947    0.568521    0.628775
   8     0.568521    0.566430    0.368898
   9     0.566430    0.567648    0.214843
------------------------------------------------------------
La raíz encontrada es: 0.567648
