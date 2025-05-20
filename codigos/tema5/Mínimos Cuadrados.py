import numpy as np

# Datos del Ejercicio 1
x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.2, 7.8, 10.3]
n = len(x)

# Variables para sumar
suma_x = sum(x)
suma_y = sum(y)
suma_xy = sum(x[i] * y[i] for i in range(n))
suma_x2 = sum(x[i] * x[i] for i in range(n))

# Calcular coeficientes de la recta: y = a * x + b
a = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x * suma_x)
b = (suma_y - a * suma_x) / n

# Calcular Error Cuadrático Medio (ECM)
suma_errores_cuadrados = 0
for i in range(n):
    y_estimado = a * x[i] + b
    error = y[i] - y_estimado
    suma_errores_cuadrados += error * error

ecm = suma_errores_cuadrados / n

# Estimar y para un x dado
x_buscado = 6
y_estimado = a * x_buscado + b

# Mostrar resultados
print(f"La recta de mínimos cuadrados es: y = {a:.4f} * x + {b:.4f}")
print(f"Error cuadrático medio (ECM): {ecm:.4f}")
print(f"Para x = {x_buscado}, el valor estimado de y es: {y_estimado:.4f}")




Output :
La recta de mínimos cuadrados es: y = 2.0300 * x + -0.0300
Error cuadrático medio (ECM): 0.0326
Para x = 6, el valor estimado de y es: 12.1500
