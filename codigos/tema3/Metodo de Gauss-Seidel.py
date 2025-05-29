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

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    # Implementación del método Gauss-Seidel
    n = len(A)
    x = np.zeros(n)  # Solución inicial (vector de ceros)
    iteraciones = 0
    
    # Iteraciones del método
    for _ in range(max_iter):
        x_nuevo = np.copy(x)
        # Actualización de cada componente de la solución
        for i in range(n):
            # Cálculo de la suma para la componente i
            suma = sum(A[i][j] * x_nuevo[j] for j in range(n) if j != i)
            # Actualización del valor de x[i]
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        
        # Cálculo del error para verificar convergencia
        error = np.linalg.norm(x_nuevo - x, ord=np.inf)
        if error < tol:
            # Mensaje de convergencia exitosa
            print(f"Convergencia alcanzada en {iteraciones + 1} iteraciones.\n")
            return x_nuevo
        
        x = x_nuevo
        iteraciones += 1
    
    # Mensaje si no converge en las iteraciones máximas
    print("Máximo número de iteraciones alcanzado. El método puede no haber convergido.\n")
    return x

# Programa principal
A, b = llenarmatriz()  # Entrada de datos
print("\nMatriz ingresada:")
mostrarmatriz(A, "Matriz de coeficientes")  # Muestra la matriz
soluciones = gauss_seidel(A, b)  # Resuelve el sistema
print("Soluciones del sistema:", soluciones)  # Muestra resultados


output:

=== MÉTODO DE GAUSS-SEIDEL PARA SISTEMAS DE ECUACIONES ===
Ingrese el número de ecuaciones (y variables): 3
Ingrese los coeficientes del sistema:
Ingrese el valor para la posición [0][0]: 4
Ingrese el valor para la posición [0][1]: -1
Ingrese el valor para la posición [0][2]: 0
Ingrese el valor para la posición [1][0]: -1
Ingrese el valor para la posición [1][1]: 4
Ingrese el valor para la posición [1][2]: -1
Ingrese el valor para la posición [2][0]: 0
Ingrese el valor para la posición [2][1]: -1
Ingrese el valor para la posición [2][2]: 4
Ingrese los términos independientes:
Ingrese el valor del término independiente en la fila 0: 2
Ingrese el valor del término independiente en la fila 1: 6
Ingrese el valor del término independiente en la fila 2: 2

Matriz ingresada:
Matriz de coeficientes:
4.00 -1.00 0.00
-1.00 4.00 -1.00
0.00 -1.00 4.00

Vector de términos independientes:
[2. 6. 2.]

Iteraciones del método Gauss-Seidel:
Iteración  Solución             Error          
---------------------------------------------
1          [0.5 1.625 0.90625]  1.625000
2          [0.90625 1.726562 0.931641] 0.281250
3          [0.931641 1.733154 0.933288] 0.025391
4          [0.933288 1.733322 0.933331] 0.001647
5          [0.933331 1.733333 0.933333] 0.000011
6          [0.933333 1.733333 0.933333] 0.000000

Convergencia alcanzada en 6 iteraciones.

Soluciones del sistema: [0.933333 1.733333 0.933333]
