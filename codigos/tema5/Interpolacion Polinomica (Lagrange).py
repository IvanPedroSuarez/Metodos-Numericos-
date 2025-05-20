# Método de interpolación polinómica de Lagrange
def interpolar_polinomio(x, y, x_buscado):
    resultado = 0
    n = len(x)

    # Suma de los términos de Lagrange
    for i in range(n):
        # Calcular el término Li(x)
        termino = y[i]

        # Multiplicar por los factores (x-xj)/(xi-xj) para j≠i
        for j in range(n):
            if j != i:
                try:
                    termino *= (x_buscado - x[j]) / (x[i] - x[j])
                except ZeroDivisionError:
                    print("Error: División por cero. Posiblemente hay valores x repetidos.")
                    return float('inf')

        resultado += termino

    return resultado

# Datos del Ejercicio 1: Función x²
x = [1, 2, 4]
y = [1, 4, 16]
x_buscado = 3
valor_real = 9  # 3²

# Realizar la interpolación
resultado = interpolar_polinomio(x, y, x_buscado)

# Mostrar resultados
print(f"Valor interpolado en x = {x_buscado}: {resultado:.4f}")
print(f"Valor real en x = {x_buscado}: {valor_real}")
print(f"Cuota de error estimada: {abs(valor_real - resultado):.4f}")
print("\nPuntos utilizados:")
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")



Output :
Valor interpolado en x = 3.0: 9.0000
Valor real en x = 3.0: 9
Cuota de error estimada: 0.0000

 Puntos utilizados:
 x = 1, y = 1
 x = 2, y = 4
 x = 4, y = 16
