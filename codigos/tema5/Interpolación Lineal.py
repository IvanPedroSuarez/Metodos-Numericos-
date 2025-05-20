import numpy as np

# Función de interpolación lineal
def interpolar_lineal(x, y, x_buscado):
    # Recorre los intervalos para encontrar dónde está x_buscado
    for i in range(len(x) - 1):
        if x[i] <= x_buscado <= x[i + 1]:
            # Obtiene los puntos del intervalo
            x0, x1 = x[i], x[i + 1]
            y0, y1 = y[i], y[i + 1]

            # Aplica la fórmula de interpolación lineal: y = y0 + (x-x0)*(y1-y0)/(x1-x0)
            resultado = y0 + (x_buscado - x0) * (y1 - y0) / (x1 - x0)
            return resultado

    # Si no encuentra un intervalo válido
    print("Error: x_buscado fuera del rango de datos.")
    return None

# Función para calcular el error
def calcular_error(valor_real, valor_interpolado):
    return abs(valor_real - valor_interpolado)

# Datos del Ejercicio 1: Función √x
x = [1, 4, 9]
y = [1.0, 2.0, 3.0]
x_buscado = 6

# Valor real para comparar (√6)
valor_real = np.sqrt(6)

# Realizar la interpolación
resultado = interpolar_lineal(x, y, x_buscado)

# Mostrar resultados
print(f"Valor interpolado en x = {x_buscado}: {resultado:.4f}")
print(f"Valor real en x = {x_buscado}: {valor_real:.4f}")
print(f"Cuota de error estimada: {calcular_error(valor_real, resultado):.4f}")
print("\nPuntos utilizados:")
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")




Output:

Valor interpolado en x = 6.0: 2.4000
Valor real en x = 6.0: 2.4495
Cuota de error estimada: 0.0495

 Puntos utilizados:
x = 1, y = 1.0
x = 4, y = 2.0
x = 9, y = 3.0
