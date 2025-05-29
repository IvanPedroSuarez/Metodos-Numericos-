Método de la Regla Falsa - Ejeemplo de ejercicio resuelto en python.

def regla_falsa(f, a, b, tolerancia=1e-6, max_iter=100):
    """
    Implementación del método de la regla falsa
    Parámetros:
    f: función a evaluar
    a, b: límites del intervalo inicial
    tolerancia: error permitido
    max_iter: número máximo de iteraciones
    """
    # Verificar si hay un cambio de signo en el intervalo
    if f(a) * f(b) >= 0:
        return None, "Error: No hay cambio de signo en el intervalo"

    iteracion = 0
    resultados = []
    c_ant = a  # Para calcular el error

    while iteracion < max_iter:
        # Calcular el punto de intersección
        c = b - (f(b) * (b - a)) / (f(b) - f(a))

        # Calcular el error relativo porcentual
        error = abs((c - c_ant) / c) * 100 if c != 0 else abs(c - c_ant)

        # Almacenar resultados
        resultados.append({
            'iteracion': iteracion + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f(c),
            'error': error
        })

        # Verificar si hemos encontrado la raíz
        if abs(f(c)) < tolerancia:
            return c, resultados

        # Actualizar intervalo
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        c_ant = c
        iteracion += 1

    return c, resultados

# Ejemplo de uso con la función del PDF: f(x) = x³ - x - 1
def f(x):
    return x**3 - x - 1

# Ejecutar el método
raiz, resultados = regla_falsa(f, 1, 2)

# Imprimir resultados en formato tabular
print("\nMétodo de la Regla Falsa para f(x) = x³ - x - 1")
print("-" * 80)
print(f"{'Iter':^6} {'a':^12} {'b':^12} {'c':^12} {'f(c)':^12} {'Error %':^12}")
print("-" * 80)

for r in resultados:
    print(f"{r['iteracion']:^6d} {r['a']:^12.6f} {r['b']:^12.6f} {r['c']:^12.6f} {r['f(c)']:^12.6f} {r['error']:^12.6f}")

print("-" * 80)
print(f"La raíz encontrada es: {raiz:.6f}")


Output

Método de la Regla Falsa para f(x) = x³ - x - 1
--------------------------------------------------------------------------------
 Iter      a           b           c          f(c)       Error %   
--------------------------------------------------------------------------------
   1     1.000000    2.000000    1.500000    0.875000    33.333333
   2     1.000000    1.500000    1.347222    0.231831    11.339869
   3     1.000000    1.347222    1.325529    0.068799    1.635833
   4     1.000000    1.325529    1.324718    0.000891    0.061338
   5     1.000000    1.324718    1.324717    0.000012    0.000079
--------------------------------------------------------------------------------
La raíz encontrada es: 1.324717
