import numpy as np

def calcular_correlacion(x, y):
    n = len(x)

    # Calcular sumas necesarias
    suma_x = sum(x)
    suma_y = sum(y)
    suma_xy = sum(x[i] * y[i] for i in range(n))
    suma_x2 = sum(x[i] * x[i] for i in range(n))
    suma_y2 = sum(y[i] * y[i] for i in range(n))

    # Calcular numerador y denominador de la fórmula de correlación
    numerador = (n * suma_xy) - (suma_x * suma_y)
    denominador = np.sqrt((n * suma_x2 - suma_x**2) * (n * suma_y2 - suma_y**2))

    # Verificar división por cero
    if denominador == 0:
        print("Error: división entre cero.")
        return 0

    # Calcular coeficiente de correlación
    return numerador / denominador

def calcular_error(r):
    # Calcular cuota de error (distancia de 1 o -1)
    return 1 - abs(r)

# Datos del Ejercicio 1: Correlación perfecta positiva
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Calcular coeficiente de correlación
r = calcular_correlacion(x, y)

# Calcular cuota de error
error = calcular_error(r)

# Mostrar resultados
print("Puntos utilizados:")
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")

print(f"\nCoeficiente de correlación: {r:.4f}")
print(f"Cuota de error: {error:.4f}")

# Interpretar el resultado
if r == 1:
    print("Correlación perfecta positiva.")
elif r == -1:
    print("Correlación perfecta negativa.")
elif r > 0:
    print("Correlación positiva.")
elif r < 0:
    print("Correlación negativa.")
else:
    print("Sin correlación.")




Output :
Puntos utilizados:
x = 1, y = 2
x = 2, y = 4
x = 3, y = 6
x = 4, y = 8
x = 5, y = 10

Coeficiente de correlación: 1.0000
Cuota de error: 0.0000
Correlación perfecta positiva.
