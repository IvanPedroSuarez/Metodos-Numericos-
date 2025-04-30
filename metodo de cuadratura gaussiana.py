import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi


def cuadratura_gaussiana_usuario():
    """
    Programa interactivo para calcular integrales definidas usando cuadratura gaussiana.
    El usuario ingresa la función y los parámetros de integración.
    """
    print("=== Calculadora de Integrales por Cuadratura Gaussiana ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'exp(-x*2)', 'sin(x)*cos(x)', 'sqrt(1+x*2)'")

    # Solicitar entrada de usuario
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de puntos gaussianos (2-5 recomendado): "))

    # Definir la función a partir del string ingresado
    def f(x):
        return eval(funcion_str)

    # Datos de nodos y pesos para cuadratura gaussiana
    nodos_pesos = {
        2: {
            'nodos': [-0.5773502691896257, 0.5773502691896257],
            'pesos': [1.0, 1.0]
        },
        3: {
            'nodos': [-0.7745966692414834, 0.0, 0.7745966692414834],
            'pesos': [0.5555555555555556, 0.8888888888888888, 0.5555555555555556]
        },
        4: {
            'nodos': [-0.8611363115940526, -0.3399810435848563,
                      0.3399810435848563, 0.8611363115940526],
            'pesos': [0.3478548451374538, 0.6521451548625461,
                      0.6521451548625461, 0.3478548451374538]
        },
        5: {
            'nodos': [-0.9061798459386640, -0.5384693101056831, 0.0,
                      0.5384693101056831, 0.9061798459386640],
            'pesos': [0.2369268850561891, 0.4786286704993665, 0.5688888888888889,
                      0.4786286704993665, 0.2369268850561891]
        }
    }

    if n not in nodos_pesos:
        print(f"\nError: Número de puntos {n} no soportado. Use valores entre 2 y 5.")
        return

    # Obtener nodos y pesos
    nodos = np.array(nodos_pesos[n]['nodos'])
    pesos = np.array(nodos_pesos[n]['pesos'])

    try:
        # Transformar nodos al intervalo [a, b]
        x_transformados = 0.5 * (b - a) * nodos + 0.5 * (a + b)

        # Evaluar la función
        fx = f(x_transformados)

        # Calcular la integral
        integral = 0.5 * (b - a) * np.dot(pesos, fx)

        # Mostrar resultados
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de puntos gaussianos: {n}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")

        # Mostrar detalles del cálculo
        print("\nDetalles del cálculo:")
        for i in range(n):
            print(f"Punto {i + 1}: x = {x_transformados[i]:.6f}, f(x) = {fx[i]:.6f}, peso = {pesos[i]:.6f}")

    except Exception as e:
        print(f"\nError al calcular la integral: {str(e)}")
        print("Revise que la función esté bien escrita y sea válida para todos los puntos en el intervalo.")


# Ejecutar el programa
if _name_ == "_main_":
    cuadratura_gaussiana_usuario()