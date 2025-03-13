# Implementación del método de eliminación gaussiana con pivoteo parcial
# Este programa permite resolver sistemas de ecuaciones lineales mediante
# la transformación de la matriz de coeficientes en una matriz triangular superior.

def llenarmatriz():
    """
    Función que permite al usuario ingresar manualmente los elementos de una matriz cuadrada.

    Returns:
        list: Matriz cuadrada de tamaño n×n con los valores ingresados por el usuario.
    """
    matriz = []
    n = int(input("Ingrese el tamaño de la matriz (n): "))

    print('Ingrese los valores de la matriz:')
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f'Ingrese el valor para la posición [{i}][{j}]: '))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrarmatriz(mat):
    """
    Función que muestra en pantalla los elementos de una matriz con formato.

    Args:
        mat (list): Matriz a mostrar.
    """
    print("Matriz:")
    for fila in mat:
        for elemento in fila:
            print(f"{elemento:.4f}", end='\t')
        print()
    print()

def gauss_pivot(matriz):
    """
    Implementa el método de eliminación gaussiana con pivoteo parcial.

    Args:
        matriz (list): Matriz de coeficientes del sistema de ecuaciones.

    Returns:
        list: Matriz triangular superior resultante o None si la matriz es singular.
    """
    n = len(matriz)
    A = [fila[:] for fila in matriz]

    print("Iniciando eliminación gaussiana con pivoteo parcial")
    print("Matriz original:")
    mostrarmatriz(A)

    for i in range(n):
        max_el = abs(A[i][i])
        max_row = i

        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k

        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            print(f"Intercambiando fila {i} con fila {max_row}")
            mostrarmatriz(A)

        if abs(A[i][i]) < 1e-10:
            print("La matriz es singular o casi singular. No se puede continuar.")
            return None

        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

            print(f"Eliminando elemento en posición [{k}][{i}] con factor {factor:.4f}")
            mostrarmatriz(A)

    print("Matriz triangular superior resultante:")
    mostrarmatriz(A)
    return A

# Menú para que el usuario elija cómo ingresar la matriz
opcion = input("Desea ingresar la matriz manualmente? (s/n): ").strip().lower()
if opcion == 's':
    matriz = llenarmatriz()
else:
    matriz = [
        [4, 2, 3],
        [2, 5, 8],
        [1, 1, 2]
    ]
    print("Usando matriz de ejemplo:")
    mostrarmatriz(matriz)

# Aplicar el método de eliminación gaussiana con pivoteo parcial
matriz_triangular = gauss_pivot(matriz)
print("Proceso de eliminación gaussiana completado.")


