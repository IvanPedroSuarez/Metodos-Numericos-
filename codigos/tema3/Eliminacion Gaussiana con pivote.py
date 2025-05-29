import numpy as np

def llenar_matriz():
    """
    Función para que el usuario ingrese la matriz de coeficientes y el vector de términos independientes.
    
    Retorna:
    - matriz: Matriz de coeficientes del sistema (numpy array)
    - vector_b: Vector de términos independientes (numpy array)
    """
    # Solicitar al usuario el número de ecuaciones/variables
    n = int(input("Ingrese el numero de ecuaciones (y variables): "))
    
    # Inicializar matriz vacía
    matriz = []
    print("Ingrese los coeficioentes del sistema: ")
    
    # Llenar la matriz fila por fila
    for i in range(n):
        fila = []
        for j in range(n):
            # Solicitar cada coeficiente de la matriz
            valor = float(input(f'Ingrese el valor para la posicion [{i}] [{j}]:'))
            fila.append(valor)
        matriz.append(fila)
    
    # Inicializar vector de términos independientes
    vector_b = []
    print("Ingrese los terminos independientes: ")
    
    # Llenar el vector de términos independientes
    for i in range(n):
        valor = float(input(f'Ingrese el valor del termino independiente en la fila {i}: '))
        vector_b.append(valor)
    
    # Convertir a arrays de numpy con tipo float para cálculos numéricos
    return np.array(matriz, dtype=float), np.array(vector_b, dtype=float)

def mostrar_matriz(matriz, nombre="Matriz"):
    """
    Función para mostrar una matriz con formato legible.
    
    Parámetros:
    - matriz: Matriz a mostrar (numpy array)
    - nombre: Nombre descriptivo para la matriz (str)
    """
    print(f"\n{nombre}:")
    # Mostrar cada fila de la matriz con 2 decimales
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_pivoteo(A, b):
    """
    Método de Eliminación Gaussiana con Pivoteo Parcial para resolver Ax = b.
    
    Parámetros:
    - A: Matriz de coeficientes (numpy array)
    - b: Vector de términos independientes (numpy array)
    
    Retorna:
    - x: Vector solución del sistema (numpy array)
    """
    n = len(A)
    # Crear matriz aumentada [A|b]
    Ab = np.hstack((A, b.reshape(-1, 1)))
    print("\nMatriz aumentada inicial:")
    mostrar_matriz(Ab, "Matriz Aumentada")

    # Eliminación hacia adelante con pivoteo parcial
    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo valor absoluto en la columna actual
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        
        # Si la fila con el máximo no es la actual, intercambiar filas
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]  # Intercambio de filas
        
        # Normalizar la fila del pivote (hacer 1 el elemento diagonal)
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Eliminación: hacer ceros en la columna debajo del pivote
        for j in range(i + 1, n):
            Ab[j] -= Ab[j, i] * Ab[i]
        
        # Mostrar estado actual de la matriz (opcional para seguimiento)
        print(f"\nMatriz después de la eliminación en la columna {i}:")
        mostrar_matriz(Ab, "Matriz Aumentada")
    
    # Sustitución regresiva para encontrar soluciones
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1:n] * x[i + 1:n])
    
    return x

if __name__ == "__main__":
    print("=== ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL ===")
    # Obtener datos del usuario
    A, b = llenar_matriz()
    
    # Mostrar matriz ingresada
    print("\nMatriz ingresada:")
    mostrar_matriz(A, "Matriz de coeficientes")
    
    # Resolver el sistema
    soluciones = gauss_pivoteo(A, b)
    
    # Mostrar resultados
    print("\nSoluciones del sistema:", soluciones)



output:

=== ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL ===
Ingrese el numero de ecuaciones (y variables): 3
Ingrese los coeficientes del sistema: 
Ingrese el valor para la posicion [0][0]: 2
Ingrese el valor para la posicion [0][1]: 1
Ingrese el valor para la posicion [0][2]: -1
Ingrese el valor para la posicion [1][0]: -3
Ingrese el valor para la posicion [1][1]: -1
Ingrese el valor para la posicion [1][2]: 2
Ingrese el valor para la posicion [2][0]: -2
Ingrese el valor para la posicion [2][1]: 1
Ingrese el valor para la posicion [2][2]: 2
Ingrese los terminos independientes: 
Ingrese el valor del termino independiente en la fila 0: 8
Ingrese el valor del termino independiente en la fila 1: -11
Ingrese el valor del termino independiente en la fila 2: -3

Matriz ingresada:
Matriz de coeficientes:
2.00 1.00 -1.00
-3.00 -1.00 2.00
-2.00 1.00 2.00

Matriz aumentada inicial:
Matriz Aumentada:
2.00 1.00 -1.00 8.00
-3.00 -1.00 2.00 -11.00
-2.00 1.00 2.00 -3.00

Intercambio de fila 0 con fila 1
Matriz después del intercambio:
Matriz Aumentada:
-3.00 -1.00 2.00 -11.00
2.00 1.00 -1.00 8.00
-2.00 1.00 2.00 -3.00

Matriz después de la eliminación en la columna 0:
Matriz Aumentada:
1.00 0.33 -0.67 3.67
0.00 1.67 0.33 15.33
0.00 1.67 0.67 4.33

Matriz después de la eliminación en la columna 1:
Matriz Aumentada:
1.00 0.33 -0.67 3.67
0.00 1.00 0.20 9.18
0.00 0.00 0.33 -11.00

Matriz después de la eliminación en la columna 2:
Matriz Aumentada:
1.00 0.33 0.00 -18.33
0.00 1.00 0.00 15.00
0.00 0.00 1.00 -33.00

Soluciones del sistema: [ 2. -1. -3.]

