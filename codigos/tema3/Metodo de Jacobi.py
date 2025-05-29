import numpy as np

def llenarmatriz():
    # Solicita al usuario el tamaño del sistema (n ecuaciones y n variables)
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    matriz = []
    
    # Llenado de la matriz de coeficientes
    print("Ingrese los coeficientes del sistema:")
    for i in range(n):
        fila = []
        for j in range(n):
            # Solicita cada elemento de la matriz
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)
    
    # Llenado del vector de términos independientes
    vector_b = []
    print("Ingrese los términos independientes:")
    for i in range(n):
        # Solicita cada término independiente
        valor = float(input(f'Ingrese el valor del término independiente en la fila {i}: '))
        vector_b.append(valor)
    
    # Convierte a arrays numpy para operaciones matemáticas
    return np.array(matriz, dtype=float), np.array(vector_b, dtype=float)

def mostrarmatriz(matriz, nombre="Matriz"):
    # Muestra la matriz con formato legible
    print(f"\n{nombre}:")
    for fila in matriz:
        # Formatea cada elemento con 2 decimales
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def jacobi(A, b, tol=1e-6, max_iter=100):
    # Implementación del método de Jacobi
    n = len(A)
    x = np.zeros(n)  # Solución inicial (vector de ceros)
    iteraciones = 0
    
    # Iteraciones del método
    for _ in range(max_iter):
        x_nuevo = np.zeros(n)  # Vector para la nueva aproximación
        # Actualización de cada componente de la solución
        for i in range(n):
            # Cálculo de la suma para la componente i
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            # Actualización del valor de x[i]
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        
        # Cálculo del error para verificar convergencia
        error = np.linalg.norm(x_nuevo - x, ord=np.inf)
        if error < tol:
            # Mensaje de convergencia exitosa
            print(f"Convergencia alcanzada en {iteraciones + 1} iteraciones.\n")
            return x_nuevo
        
        x = x_nuevo  # Actualiza la solución para la próxima iteración
        iteraciones += 1
    
    # Mensaje si no converge en las iteraciones máximas
    print("Máximo número de iteraciones alcanzado. El método puede no haber convergido.\n")
    return x

# Programa principal
A, b = llenarmatriz()  # Entrada de datos
print("\nMatriz ingresada:")
mostrarmatriz(A, "Matriz de coeficientes")  # Muestra la matriz
soluciones = jacobi(A, b)  # Resuelve el sistema
print("Soluciones del sistema:", soluciones)  # Muestra resultados



output:

=== MÉTODO DE JACOBI PARA SISTEMAS DE ECUACIONES ===
Ingrese el número de ecuaciones (y variables): 3
Ingrese los coeficientes del sistema:
Ingrese el valor para la posición [0][0]: 10
Ingrese el valor para la posición [0][1]: -1
Ingrese el valor para la posición [0][2]: 2
Ingrese el valor para la posición [1][0]: -1
Ingrese el valor para la posición [1][1]: 11
Ingrese el valor para la posición [1][2]: -1
Ingrese el valor para la posición [2][0]: 2
Ingrese el valor para la posición [2][1]: -1
Ingrese el valor para la posición [2][2]: 10
Ingrese los términos independientes:
Ingrese el valor del término independiente en la fila 0: 6
Ingrese el valor del término independiente en la fila 1: 25
Ingrese el valor del término independiente en la fila 2: -11

Matriz ingresada:
Matriz de coeficientes:
10.00 -1.00 2.00
-1.00 11.00 -1.00
2.00 -1.00 10.00

Vector de términos independientes:
[ 6. 25. -11.]

Iteraciones del método Jacobi:
Iteración  Solución                        Error          
-------------------------------------------------------
1          [0.6 2.272727 -1.1]             2.272727
2          [1.047273 1.715909 -0.805227]   0.556818
3          [0.932636 2.053306 -1.049345]   0.337397
4          [1.015199 1.953696 -0.968109]    0.082563
5          [0.988991 2.011415 -1.010285]   0.057719
6          [1.003199 1.992238 -0.994522]   0.015924
7          [0.998128 2.002307 -1.003072]   0.010069
8          [1.000625 1.99867 -0.999121]    0.003951
9          [0.999767 2.000448 -1.000747]   0.002396
10         [1.000078 1.999823 -0.999943]   0.000899
11         [0.999985 2.000091 -1.000144]   0.000555
12         [1.000008 1.999958 -0.999991]   0.000208

Convergencia alcanzada en 12 iteraciones.

Soluciones del sistema: [1. 2. -1.]
