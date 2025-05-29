import numpy as np

def funcion_con_error_division_cero():
    """
    Función que demuestra el error de división por cero en interpolación lineal.

    Esta función está diseñada para fallar cuando se tienen puntos duplicados
    consecutivos en el eje X y se busca interpolar exactamente en esa coordenada.

    Returns:
        float: Valor interpolado (si no hay error)

    Raises:
        ZeroDivisionError: Cuando hay puntos duplicados consecutivos en X
                          y x_buscado coincide con ellos
    """

    # Datos problemáticos: puntos duplicados al inicio
    x = [2.0, 2.0, 4.0, 6.0]  # x[0] = x[1] = 2.0 (DUPLICADOS)
    y = [1.0, 5.0, 8.0, 12.0] # Diferentes valores y para el mismo x
    x_buscado = 2.0            # Coincide exactamente con los duplicados

    # Algoritmo de interpolación lineal (destinado a fallar)
    for i in range(len(x) - 1):
        if x[i] <= x_buscado <= x[i + 1]:  # Condición se cumple para [2.0, 2.0]
            x0, x1 = x[i], x[i + 1]        # x0 = x1 = 2.0
            y0, y1 = y[i], y[i + 1]        # y0 = 1.0, y1 = 5.0

            # ERROR: División por cero cuando (x1 - x0) = (2.0 - 2.0) = 0
            resultado = y0 + (x_buscado - x0) * (y1 - y0) / (x1 - x0)
            return resultado

    return None

# Ejecutar la función
try:
    resultado = funcion_con_error_division_cero()
except ZeroDivisionError as e:
    print(f"ERROR: {e}")



output
ERROR: float division by zero
