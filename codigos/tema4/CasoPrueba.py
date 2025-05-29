import numpy as np
import matplotlib.pyplot as plt

def integral_trapecio_interactivo():
    # Imprime el título y las instrucciones para el usuario
    print("=== Calculadora de Integrales por Método del Trapecio ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'")

    # Solicita al usuario la función, los límites y el número de subintervalos
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0): "))

    # Verifica que el número de subintervalos sea válido
    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return

    # Define la función a integrar usando eval en un entorno seguro
    def f(x):
        return eval(funcion_str, {"__builtins__": None}, {
            "x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "np": np
        })

    try:
        # Calcula el ancho de cada subintervalo
        h = (b - a) / n
        # Genera los puntos x y evalúa la función en esos puntos
        x_points = np.linspace(a, b, n + 1)
        y_points = f(x_points)

        # Verifica si hay valores no definidos (NaN o infinito) en la evaluación
        if np.any(np.isnan(y_points)) or np.any(np.isinf(y_points)):
            raise ValueError("La función no está definida en todo el intervalo de integración.")

        # Calcula la integral usando el método del trapecio
        integral = h * (0.5 * y_points[0] + 0.5 * y_points[-1] + np.sum(y_points[1:-1]))

        # Muestra los resultados principales
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")

        # Si n es pequeño, muestra el detalle de cada trapecio
        if n <= 10:
            print("\nDetalles del cálculo:")
            print(f"{'Intervalo':<10} {'x_i':<15} {'f(x_i)':<15} {'Área':<15}")
            print("-" * 55)
            for i in range(n):
                area = h * (y_points[i] + y_points[i + 1]) / 2
                print(f"{i}-{i + 1:<7} {x_points[i]:<15.6f} {y_points[i]:<15.6f} {area:<15.6f}")
            print("\nSuma de áreas de todos los trapecios:", integral)

        # Llama a la función para graficar los trapecios
        graficar_trapecios(f, x_points, y_points, a, b)

    except Exception as e:
        # Captura cualquier error y muestra un mensaje explicativo
        print("\n=== Error de evaluación ===")
        print(f"Error al calcular la integral: {str(e)}")
        print("Esto puede deberse a que la función no está definida en todo el intervalo,")
        print("por ejemplo, divisiones por cero, raíces negativas, o valores infinitos.")
        print("Estas son limitaciones del manejo numérico en Python.")

def graficar_trapecios(f, x_points, y_points, a, b):
    # Genera puntos para graficar la curva de la función
    x_curve = np.linspace(a, b, 1000)
    y_curve = f(x_curve)

    # Crea la figura y grafica la función y los trapecios
    plt.figure(figsize=(10, 6))
    plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Función')
    for i in range(len(x_points) - 1):
        x_trap = [x_points[i], x_points[i], x_points[i + 1], x_points[i + 1]]
        y_trap = [0, y_points[i], y_points[i + 1], 0]
        plt.fill(x_trap, y_trap, 'r', alpha=0.2)
    plt.title('Método del Trapecio para Integración Numérica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.savefig('trapezoidal_integral.png')
    plt.close()

if __name__ == "__main__":
    integral_trapecio_interactivo()

# --- Output 


=== Calculadora de Integrales por Método del Trapecio ===

Instrucciones:
1. Ingrese la función a integrar usando x como variable
2. Use funciones matemáticas como sin(), cos(), exp(), etc.
3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'

Ingrese la función a integrar (en términos de x): 1/x
Ingrese el límite inferior de integración (a): -1
Ingrese el límite superior de integración (b): 1
Ingrese el número de subintervalos (n > 0): 4

=== Error de evaluación ===
Error al calcular la integral: La función no está definida en todo el intervalo de integración.
Esto puede deberse a que la función no está definida en todo el intervalo,
por ejemplo, divisiones por cero, raíces negativas, o valores infinitos.
Estas son limitaciones del manejo numérico en Python.

# --- Explicación de cuándo falla ---

# El código puede fallar o dar errores cuando:
# 1) La función ingresada no es válida o tiene errores de sintaxis.
# 2) Se usan funciones o variables no definidas en el entorno seguro del eval().
# 3) El número de subintervalos (n) es cero o negativo, lo cual se valida y detiene el proceso.
# 4) El límite inferior y superior no son numéricos o no tienen sentido (por ejemplo, b < a, aunque el método igual funciona).
# 5) Al evaluar la función en puntos, si la función es discontinua o tiene valores no definidos en el intervalo, puede generar errores o valores NaN.
# 
# El programa captura excepciones y muestra un mensaje de error para que el usuario revise la función o los datos ingresados.
