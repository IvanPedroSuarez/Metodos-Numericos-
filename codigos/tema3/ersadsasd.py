import numpy as np

def llenar_matriz():
  """
  funcion para que el usuario infgrese la matriz de coeficientes y el vector de terminos independientes.
  """
  n = int (input("Ingrese el numero de ecuaciones (y variables): "))
  matriz = []
  print("Ingrese los coeficioentes del sistema: ")
  for i in range(n):
    fila = []
    for j in range(n):
      valor = float(input(f'Ingrese el valor para la posicion [{i}] [{j}]:'))
      fila.append(valor)
    matriz.append(fila)

vector:b = []
print("Ingrese los terminos independientes: ")
for i in range(n):
   valor = float(input(f'Ingrese el valor del termino independiente en la fila {i}: '))
  vector_b.append(valor)
return np.array(matriz, dtype = float), no.arrary(vector_b, dtype=float)

def mostrar_matriz(matriz, nombre="Matriz"):
    """
    Función para mostrar una matriz con formato legible.
    """
    print(f"\n{nombre}:")
    for fila in matriz:
        print(" ".join(f"{elemento:.2f}" for elemento in fila))
    print()

def gauss_pivoteo(A, b):
    """
    Método de Eliminación Gaussiana con Pivoteo Parcial para resolver Ax = b.

    Parámetros:
    - A: Matriz de coeficientes
    - b: Vector de términos independientes

    Retorna:
    - x: Vector solución
    """
    n = len(A)
    # Matriz aumentada [A|b]
    Ab = np.hstack((A, b.reshape(-1, 1)))
    print("\nMatriz aumentada inicial:")
    mostrar_matriz(Ab, "Matriz Aumentada")

 
    # Eliminación hacia adelante con pivoteo parcial
    for i in range(n):
        # Pivoteo parcial: intercambiar filas si el pivote es pequeño
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]  # Intercambio de filas
        
        # Hacer 1 el pivote dividiendo la fila
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Hacer ceros en la columna debajo del pivote
        for j in range(i + 1, n):
            Ab[j] -= Ab[j, i] * Ab[i]
           print(f"\nMatriz después de la eliminación en la columna {i}:")
        mostrar_matriz(Ab, "Matriz Aumentada")
    
    # Sustitución regresiva para encontrar soluciones
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1:n] * x[i + 1:n])
    
    return x

if __name__ == "__main__":
    print("=== ELIMINACIÓN GAUSSIANA CON PIVOTEO PARCIAL ===")
    A, b = llenar_matriz()
    print("\nMatriz ingresada:")
    mostrar_matriz(A, "Matriz de coeficientes")

    soluciones = gauss_pivoteo(A, b)
    print("\nSoluciones del sistema:", soluciones)

