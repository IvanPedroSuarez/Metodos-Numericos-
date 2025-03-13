# Implementación del método de eliminación gaussiana con pivoteo parcial
# Este programa permite resolver sistemas de ecuaciones lineales mediante
# la transformación de la matriz de coeficientes en una matriz triangular superior.

def llenarmatriz():
    """
    Función que permite al usuario ingresar manualmente los elementos de una matriz cuadrada.

    Returns:
        list: Matriz cuadrada de tamaño n×n con los valores ingresados por el usuario.
    """
    global matriz
    matriz = []
    n = int(input("Ingrese el tamaño de la matriz (n): "))

    print('Método para llenar una matriz')
    for i in range(n):
        fila = []
        for j in range(n):
            # Solicita cada elemento de la matriz
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
            # Muestra cada elemento con 4 decimales
            print(f"{elemento:.4f}", end='\	')
        print()  # Salto de línea al final de cada fila
    print()  # Línea en blanco después de mostrar la matriz


def gauss_pivot(matriz):
    """
    Implementa el método de eliminación gaussiana con pivoteo parcial.

    El pivoteo parcial selecciona el elemento de mayor valor absoluto en cada columna
    como pivote para mejorar la estabilidad numérica del método.

    Args:
        matriz (list): Matriz de coeficientes del sistema de ecuaciones.

    Returns:
        list: Matriz triangular superior resultante o None si la matriz es singular.
    """
    n = len(matriz)
    # Crear una copia de la matriz para no modificar la original
    A = [fila[:] for fila in matriz]

    print("Iniciando eliminación gaussiana con pivoteo parcial")
    print("Matriz original:")
    mostrarmatriz(A)

    # Proceso de eliminación gaussiana con pivoteo
    for i in range(n):
        # Paso 1: Encontrar el pivote máximo en la columna i (pivoteo parcial)
        max_el = abs(A[i][i])  # Valor absoluto del elemento diagonal
        max_row = i  # Fila del elemento diagonal

        # Buscar el elemento de mayor valor absoluto en la columna i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k

        # Intercambiar filas si es necesario (pivoteo)
        if max_row != i:
            # Intercambio de filas para colocar el pivote máximo en la diagonal
            A[i], A[max_row] = A[max_row], A[i]
            print(f"Intercambiando fila {i} con fila {max_row}")
            mostrarmatriz(A)

        # Verificar si el pivote es cero (matriz singular)
        if abs(A[i][i]) < 1e-10:
            print("La matriz es singular o casi singular. No se puede continuar.")
            return None

        # Paso 2: Eliminar los elementos debajo del pivote (hacer ceros)
        for k in range(i + 1, n):
            # Calcular el factor de eliminación
            factor = A[k][i] / A[i][i]

            # Actualizar los elementos de la fila k
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

            print(f"Eliminando elemento en posición [{k}][{i}] con factor {factor:.4f}")
            mostrarmatriz(A)

    print("Matriz triangular superior resultante:")
    mostrarmatriz(A)
    return A


# Ejemplo con una matriz predefinida para evitar la entrada manual
matriz_ejemplo = [
    [4, 2, 3],  # Primera fila de la matriz
    [2, 5, 8],  # Segunda fila de la matriz
    [1, 1, 2]  # Tercera fila de la matriz
]

print("Demostración de eliminación gaussiana con pivoteo parcial")
print("--------------------------------------------------------")
print("Usando matriz de ejemplo:")
mostrarmatriz(matriz_ejemplo)

# Aplicar el método de eliminación gaussiana con pivoteo parcial
matriz_triangular = gauss_pivot(matriz_ejemplo)

print("Proceso de eliminación gaussiana completado.")

# Si quieres usar la función de llenar matriz manualmente, descomenta estas líneas:
# matriz = llenarmatriz()
# matriz_triangular = gauss_pivot(matriz)

# Nota: Este código solo realiza la eliminación gaussiana para obtener una matriz triangular superior.
# Para resolver completamente un sistema de ecuaciones, se necesitaría implementar la sustitución hacia atrás.