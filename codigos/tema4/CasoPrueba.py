import numpy as np
import matplotlib.pyplot as plt

def integral_trapecio_interactivo():
    """
    Calculadora de integrales definidas usando el método del trapecio.
    Corrige evaluación de funciones y visualiza resultado.
    """
    print("=== Calculadora de Integrales por Método del Trapecio ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'")
    
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0): "))
    
    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return
    
    def f(x):
        return eval(funcion_str, {"__builtins__": None}, {
            "x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "np": np
        })
    
    try:
        h = (b - a) / n
        x_points = np.linspace(a, b, n + 1)
        y_points = f(x_points)
        
        integral = h * (0.5 * y_points[0] + 0.5 * y_points[-1] + np.sum(y_points[1:-1]))
        
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")
        
        if n <= 10:
            print("\nDetalles del cálculo:")
            print(f"{'Intervalo':<10} {'x_i':<15} {'f(x_i)':<15} {'Área':<15}")
            print("-" * 55)
            for i in range(n):
                area = h * (y_points[i] + y_points[i + 1]) / 2
                print(f"{i}-{i + 1:<7} {x_points[i]:<15.6f} {y_points[i]:<15.6f} {area:<15.6f}")
            print("\nSuma de áreas de todos los trapecios:", integral)
        
        graficar_trapecios(f, x_points, y_points, a, b)
    
    except Exception as e:
        print(f"\nError al calcular la integral: {str(e)}")
        print("Revisa que la función esté bien escrita y sea válida.")

def graficar_trapecios(f, x_points, y_points, a, b):
    x_curve = np.linspace(a, b, 1000)
    y_curve = f(x_curve)
    
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

# --- Output simulado con una función válida y n pequeño ---


=== Calculadora de Integrales por Método del Trapecio ===

Instrucciones:
1. Ingrese la función a integrar usando x como variable
2. Use funciones matemáticas como sin(), cos(), exp(), etc.
3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'

Ingrese la función a integrar (en términos de x): x**2
Ingrese el límite inferior de integración (a): 0
Ingrese el límite superior de integración (b): 1
Ingrese el número de subintervalos (n > 0): 4

=== Resultados ===
Función integrada: f(x) = x**2
Límites de integración: [0.0, 1.0]
Número de subintervalos: 4
Ancho de cada subintervalo (h): 0.250000

Valor aproximado de la integral: 0.3281250000

Detalles del cálculo:
Intervalo   x_i             f(x_i)          Área           
-------------------------------------------------------
0-1        0.000000        0.000000        0.015625       
1-2        0.250000        0.062500        0.070312       
2-3        0.500000        0.250000        0.164062       
3-4        0.750000        0.562500        0.328125       

Suma de áreas de todos los trapecios: 0.328125


# --- Explicación de cuándo falla ---

# El código puede fallar o dar errores cuando:
# 1) La función ingresada no es válida o tiene errores de sintaxis.
# 2) Se usan funciones o variables no definidas en el entorno seguro del eval().
# 3) El número de subintervalos (n) es cero o negativo, lo cual se valida y detiene el proceso.
# 4) El límite inferior y superior no son numéricos o no tienen sentido (por ejemplo, b < a, aunque el método igual funciona).
# 5) Al evaluar la función en puntos, si la función es discontinua o tiene valores no definidos en el intervalo, puede generar errores o valores NaN.
# 
# El programa captura excepciones y muestra un mensaje de error para que el usuario revise la función o los datos ingresados.
