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

def mostrar_matriz(matriz):
    """
    Muestra la matriz en formato legible con 2 decimales.
    """
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_jordan(matriz):
    """
    Implementación del método de eliminación de Gauss-Jordan con pivoteo parcial.
    
    Args:
        matriz: Matriz aumentada del sistema de ecuaciones.
    
    Returns:
        np.array: Vector con las soluciones del sistema.
    
    Raises:
        ValueError: Si el sistema no tiene solución única.
    """
    n = len(matriz)
    
    for i in range(n):
        # Pivoteo parcial: buscar el máximo en la columna actual
        max_fila = max(range(i, n), key=lambda k: abs(matriz[k, i]))
        if i != max_fila:
            matriz[[i, max_fila]] = matriz[[max_fila, i]]  # Intercambio de filas
        
        pivote = matriz[i, i]
        if pivote == 0:
            raise ValueError("El sistema no tiene solución única.")
        
        # Normalizar la fila del pivote
        matriz[i] = matriz[i] / pivote
        
        # Eliminación hacia adelante y atrás
        for j in range(n):
            if i != j:
                factor = matriz[j, i]
                matriz[j] = matriz[j] - factor * matriz[i]
        
        print(f"\nPaso {i + 1}:")
        mostrar_matriz(matriz)
    
    return matriz[:, -1]

if __name__ == "__main__":
    print("=== ELIMINACIÓN GAUSS-JORDAN CON PIVOTEO PARCIAL ===")
    matriz = llenar_matriz()
    
    print("\nMatriz ingresada:")
    mostrar_matriz(matriz)
    
    try:
        soluciones = gauss_jordan(matriz)
        print("\nSoluciones del sistema:", soluciones)
    except ValueError as e:
        print(f"\nError: {e}")




output:

=== ELIMINACIÓN GAUSS-JORDAN CON PIVOTEO PARCIAL ===
Ingrese el número de ecuaciones (y variables): 3
Ingrese los coeficientes del sistema, incluyendo los términos independientes:
Ingrese el valor para la posición [0][0]: 2
Ingrese el valor para la posición [0][1]: 1
Ingrese el valor para la posición [0][2]: -1
Ingrese el valor para la posición [0][3]: 8
Ingrese el valor para la posición [1][0]: -3
Ingrese el valor para la posición [1][1]: -1
Ingrese el valor para la posición [1][2]: 2
Ingrese el valor para la posición [1][3]: -11
Ingrese el valor para la posición [2][0]: -2
Ingrese el valor para la posición [2][1]: 1
Ingrese el valor para la posición [2][2]: 2
Ingrese el valor para la posición [2][3]: -3

Matriz ingresada:
2.00 1.00 -1.00 8.00
-3.00 -1.00 2.00 -11.00
-2.00 1.00 2.00 -3.00


Intercambio de fila 0 con fila 1:
-3.00 -1.00 2.00 -11.00
2.00 1.00 -1.00 8.00
-2.00 1.00 2.00 -3.00


Paso 1 (Eliminación completa para variable x_0):
1.00 0.33 -0.67 3.67
0.00 1.67 0.33 15.33
0.00 1.67 0.67 4.33


Paso 2 (Eliminación completa para variable x_1):
1.00 0.00 -0.80 -1.80
0.00 1.00 0.20 9.20
0.00 0.00 0.33 -11.00


Paso 3 (Eliminación completa para variable x_2):
1.00 0.00 0.00 2.00
0.00 1.00 0.00 -1.00
0.00 0.00 1.00 -33.00


Soluciones del sistema: [  2.  -1. -33.]
