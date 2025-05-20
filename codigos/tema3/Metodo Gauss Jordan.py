import numpy as np

def llenar_matriz():
    """
    Función para llenar la matriz aumentada con valores ingresados por el usuario.
    La matriz incluye los coeficientes y la columna de términos independientes.
    """
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    matriz = []
    print("Ingrese los coeficientes del sistema, incluyendo los términos independientes:")
    
    for i in range(n):
        fila = []
        for j in range(n + 1):  # +1 para la columna de términos independientes
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)
    
    return np.array(matriz, dtype=float)
