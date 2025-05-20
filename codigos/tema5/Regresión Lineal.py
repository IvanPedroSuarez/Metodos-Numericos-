import numpy as np

def calcular_regresion_lineal(x, y):
    n = len(x)

    # Verificar que los arreglos tengan la misma longitud
    if len(y) != n:
        raise ValueError("Los arreglos deben tener la misma longitud")

    # Calcular las sumas necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_xx = sum(x[i] * x[i] for i in range(n))

    # Calcular pendiente (m) e intersección (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - m * sum_x) / n

    return m, b

def calcular_errores(x, y, m, b):
    n = len(x)
    sum_error_abs = 0
    sum_error_porcentual = 0

    for i in range(n):
        y_estimado = m * x[i] + b
        error_abs = abs(y[i] - y_estimado)
        error_porcentual = (error_abs / y[i]) * 100 if y[i] != 0 else 0

        sum_error_abs += error_abs
        sum_error_porcentual += error_porcentual

    error_abs_promedio = sum_error_abs / n
    error_porcentual_promedio = sum_error_porcentual / n

    return error_abs_promedio, error_porcentual_promedio

# Datos del Ejercicio 1: Predicción de temperatura
x = [8, 12, 14, 16]  # Hora del día
y = [15, 22, 25, 24]  # Temperatura

# Calcular regresión lineal
m, b = calcular_regresion_lineal(x, y)

# Calcular errores
error_abs_promedio, error_porcentual_promedio = calcular_errores(x, y, m, b)

# Mostrar resultados
print(f"Ecuación de la recta: y = {m:.4f}x + {b:.4f}")
print(f"Error absoluto promedio: {error_abs_promedio:.4f}")
print(f"Error porcentual promedio: {error_porcentual_promedio:.2f}%")

# Predecir temperatura a las 10 horas
x_pred = 10
y_pred = m * x_pred + b
print(f"\nTemperatura estimada a las {x_pred} horas: {y_pred:.2f}°C")

Output :
Ecuación de la recta: y = 1.2286x + 6.1429
Error absoluto promedio: 1.3857
Error porcentual promedio: 6.42%

Temperatura estimada a las 10 horas: 18.43°C
