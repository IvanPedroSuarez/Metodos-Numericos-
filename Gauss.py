def ingresar_sistema():
    """
    Permite al usuario ingresar el sistema de ecuaciones (matriz A y vector b).

    Returns:
        tuple: Matriz de coeficientes A y vector de términos independientes b.
    """
    n = int(input("Ingrese el número de ecuaciones (tamaño de la matriz): "))
    A = []
    b = []

    print("Ingrese los coeficientes de la matriz A:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1} separada por espacios: ").split()))
        if len(fila) != n:
            print("Error: Debe ingresar exactamente", n, "coeficientes.")
            return None, None
        A.append(fila)

    print("Ingrese los valores del vector b:")
    for i in range(n):
        b.append(float(input(f"b[{i + 1}]: ")))

    return A, b


def mostrar_sistema(A, b):
    """
    Muestra el sistema de ecuaciones en forma de matriz aumentada.
    """
    n = len(A)
    print("\nSistema de ecuaciones (matriz aumentada):")
    for i in range(n):
        fila = ' '.join(f"{A[i][j]:8.4f}" for j in range(n))
        print(f"{fila} | {b[i]:8.4f}")
    print()


def gauss_eliminacion(A, b):
    """
    Aplica el método de eliminación gaussiana para resolver el sistema Ax = b.
    """
    n = len(A)

    for k in range(n):
        # Verificar que el pivote no sea cero
        if abs(A[k][k]) < 1e-10:
            print("Error: Pivote cero encontrado. El sistema podría ser singular.")
            return None

        # Eliminación hacia adelante
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

        mostrar_sistema(A, b)

    # Sustitución hacia atrás
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sumatoria = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sumatoria) / A[i][i]

    return x


# Programa principal
A, b = ingresar_sistema()
if A and b:
    mostrar_sistema(A, b)
    solucion = gauss_eliminacion(A, b)
    if solucion:
        print("\nSolución del sistema:")
        for i, val in enumerate(solucion):
            print(f"x[{i + 1}] = {val:.4f}")
