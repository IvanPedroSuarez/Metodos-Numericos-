import numpy as np

def llenar_matriz():
    """
    Función para llenar la matriz aumentada con valores ingresados por el usuario.
    La matriz incluye los coeficientes y la columna de términos independientes.
    
    Retorna:
    - np.array: Matriz aumentada del sistema de ecuaciones (n x n+1)
    """
    # Solicitar al usuario el número de ecuaciones/variables
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    
    # Inicializar matriz vacía
    matriz = []
    print("Ingrese los coeficientes del sistema, incluyendo los términos independientes:")
    
    # Llenar la matriz aumentada [A|b]
    for i in range(n):
        fila = []
        # Para cada fila, pedir n coeficientes + 1 término independiente
        for j in range(n + 1):
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)
    
    # Convertir a array numpy con tipo float para cálculos numéricos
    return np.array(matriz, dtype=float)

def mostrar_matriz(matriz):
    """
    Muestra la matriz en formato legible con 2 decimales.
    
    Parámetros:
    - matriz: Matriz a mostrar (numpy array)
    """
    # Mostrar cada fila de la matriz con 2 decimales
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_jordan(matriz):
    """
    Implementación del método de eliminación de Gauss-Jordan con pivoteo parcial.
    
    Args:
        matriz: Matriz aumentada del sistema de ecuaciones [A|b] (numpy array)
    
    Returns:
        np.array: Vector con las soluciones del sistema
    
    Raises:
        ValueError: Si el sistema no tiene solución única (matriz singular)
    """
    n = len(matriz)
    
    # Proceso de eliminación para cada columna/pivote
    for i in range(n):
        # Pivoteo parcial: buscar el máximo en la columna actual (desde la diagonal hacia abajo)
        max_fila = max(range(i, n), key=lambda k: abs(matriz[k, i]))
        
        # Si el máximo no está en la diagonal, intercambiar filas
        if i != max_fila:
            matriz[[i, max_fila]] = matriz[[max_fila, i]]  # Intercambio de filas
        
        # Obtener el valor del pivote
        pivote = matriz[i, i]
        
        # Verificar si el sistema tiene solución única
        if pivote == 0:
            raise ValueError("El sistema no tiene solución única.")
        
        # Normalizar la fila del pivote (hacer 1 el elemento diagonal)
        matriz[i] = matriz[i] / pivote
        
        # Eliminación hacia adelante y atrás (Gauss-Jordan)
        for j in range(n):
            if i != j:  # No operar sobre la fila del pivote actual
                factor = matriz[j, i]  # Elemento a eliminar
                matriz[j] = matriz[j] - factor * matriz[i]  # Operación de eliminación
        
        # Mostrar el estado de la matriz en cada paso
        print(f"\nPaso {i + 1}:")
        mostrar_matriz(matriz)
    
    # La solución está en la última columna de la matriz reducida
    return matriz[:, -1]

if __name__ == "__main__":
    print("=== ELIMINACIÓN GAUSS-JORDAN CON PIVOTEO PARCIAL ===")
    
    # Obtener la matriz aumentada del usuario
    matriz = llenar_matriz()
    
    # Mostrar la matriz ingresada
    print("\nMatriz ingresada:")
    mostrar_matriz(matriz)
    
    try:
        # Resolver el sistema usando Gauss-Jordan
        soluciones = gauss_jordan(matriz)
        print("\nSoluciones del sistema:", soluciones)
    except ValueError as e:
        # Manejar caso de sistema sin solución única
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
