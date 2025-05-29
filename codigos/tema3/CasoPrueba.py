import numpy as np

def llenar_matriz():
    """
    Función para llenar la matriz aumentada con valores ingresados por el usuario.
    La matriz incluye los coeficientes y la columna de términos independientes.
    
    Retorna:
    - np.array: Matriz aumentada del sistema de ecuaciones (n x n+1)
    """
    n = int(input("Ingrese el número de ecuaciones (y variables): "))
    matriz = []
    print("Ingrese los coeficientes del sistema, incluyendo los términos independientes:")
    for i in range(n):
        fila = []
        for j in range(n + 1):
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)
    return np.array(matriz, dtype=float)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_jordan(matriz):
    n = len(matriz)
    for i in range(n):
        max_fila = max(range(i, n), key=lambda k: abs(matriz[k, i]))
        if i != max_fila:
            matriz[[i, max_fila]] = matriz[[max_fila, i]]
        pivote = matriz[i, i]
        if pivote == 0:
            raise ValueError("El sistema no tiene solución única.")
        matriz[i] = matriz[i] / pivote
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



# Output simulado para entrada inconsistente:

"""
=== ELIMINACIÓN GAUSS-JORDAN===
Ingrese el número de ecuaciones (y variables): 2
Ingrese los coeficientes del sistema, incluyendo los términos independientes:
Ingrese el valor para la posición [0][0]: 1
Ingrese el valor para la posición [0][1]: -2
Ingrese el valor para la posición [0][2]: 1
Ingrese el valor para la posición [1][0]: 2
Ingrese el valor para la posición [1][1]: -4
Ingrese el valor para la posición [1][2]: 3

Matriz ingresada:
1.00 -2.00 1.00
2.00 -4.00 3.00

Paso 1:
1.00 -2.00 1.00
0.00 0.00 1.00

Error: El sistema no tiene solución única.
"""

# Explicación:

# El método falla cuando el pivote es cero y no hay filas para intercambiar que tengan un valor distinto de cero en esa columna.
# Esto indica que el sistema no tiene solución única (puede ser inconsistente o tener infinitas soluciones).
# En el ejemplo, las filas son linealmente dependientes pero con términos independientes que no concuerdan, lo que genera inconsistencia.
# Por eso el algoritmo detecta este caso y lanza un error para evitar cálculos inválidos.
