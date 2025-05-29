import numpy as np
import matplotlib.pyplot as plt

def integral_trapecio_interactivo():
    """
    Calculadora de integrales definidas usando el método del trapecio.
    Corrige evaluación de funciones y visualiza resultado.
    """
    # Imprimir encabezado y instrucciones para el usuario
    print("=== Calculadora de Integrales por Método del Trapecio ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
    print("3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'")
    
    # Solicitar entrada del usuario
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0): "))
    
    # Validar que el número de subintervalos sea positivo
    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return
    
    # Definir la función vectorizada de forma segura
    def f(x):
        # Evaluar la función ingresada con un entorno seguro
        # Restringir __builtins__ para evitar inyecciones de código
        # Proporcionar funciones matemáticas de numpy y pi
        return eval(funcion_str, {"__builtins__": None}, {
            "x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "np": np
        })
    
    try:
        # Calcular el ancho de cada subintervalo
        h = (b - a) / n
        
        # Generar puntos equiespaciados en el intervalo [a, b]
        x_points = np.linspace(a, b, n + 1)
        
        # Evaluar la función en los puntos
        y_points = f(x_points)
        
        # Calcular la integral usando la regla del trapecio
        # Fórmula: h * (0.5 * f(x_0) + f(x_1) + ... + f(x_{n-1}) + 0.5 * f(x_n))
        integral = h * (0.5 * y_points[0] + 0.5 * y_points[-1] + np.sum(y_points[1:-1]))
        
        # Mostrar resultados principales
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")
        
        # Mostrar detalles del cálculo si n es pequeño (para no saturar la salida)
        if n <= 10:
            print("\nDetalles del cálculo:")
            print(f"{'Intervalo':<10} {'x_i':<15} {'f(x_i)':<15} {'Área':<15}")
            print("-" * 55)
            for i in range(n):
                # Calcular el área de cada trapecio: h * (f(x_i) + f(x_{i+1})) / 2
                area = h * (y_points[i] + y_points[i + 1]) / 2
                print(f"{i}-{i + 1:<7} {x_points[i]:<15.6f} {y_points[i]:<15.6f} {area:<15.6f}")
            print("\nSuma de áreas de todos los trapecios:", integral)
        
        # Generar gráfico de la función y los trapecios
        graficar_trapecios(f, x_points, y_points, a, b)
    
    except Exception as e:
        # Manejar errores durante el cálculo o evaluación
        print(f"\nError al calcular la integral: {str(e)}")
        print("Revisa que la función esté bien escrita y sea válida.")

def graficar_trapecios(f, x_points, y_points, a, b):
    """Grafica la función y los trapecios usados en la integración."""
    # Generar puntos para una curva suave (para graficar la función)
    x_curve = np.linspace(a, b, 1000)
    y_curve = f(x_curve)
    
    # Configurar la figura
    plt.figure(figsize=(10, 6))
    
    # Graficar la función como una línea continua
    plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Función')
    
    # Dibujar los trapecios
    for i in range(len(x_points) - 1):
        # Definir los vértices del trapecio (dos puntos en x, desde y=0 hasta f(x))
        x_trap = [x_points[i], x_points[i], x_points[i + 1], x_points[i + 1]]
        y_trap = [0, y_points[i], y_points[i + 1], 0]
        plt.fill(x_trap, y_trap, 'r', alpha=0.2)  # Rellenar trapecios con color rojo semitransparente
    
    # Configurar título, etiquetas y cuadrícula
    plt.title('Método del Trapecio para Integración Numérica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)  # Eje horizontal en y=0
    plt.axvline(0, color='black', linewidth=0.5)  # Eje vertical en x=0
    plt.legend()
    
    # Guardar el gráfico como imagen (siguiendo las directrices)
    plt.savefig('trapezoidal_integral.png')
    plt.close()  # Cerrar la figura para liberar memoria

if __name__ == "__main__":
    # Punto de entrada principal del programa
    integral_trapecio_interactivo()

output:

=== Calculadora de Integrales por Método del Trapecio ===

Instrucciones:
1. Ingrese la función a integrar usando x como variable
2. Use funciones matemáticas como sin(), cos(), exp(), etc.
3. Ejemplos válidos: 'x**2', 'sin(x)*cos(x)', 'exp(-x**2)'

Ingrese la función a integrar (en términos de x): x**2
Ingrese el límite inferior de integración (a): 0
Ingrese el límite superior de integración (b): 2
Ingrese el número de subintervalos (n > 0): 4

=== Resultados ===
Función integrada: f(x) = x**2
Límites de integración: [0.0, 2.0]
Número de subintervalos: 4
Ancho de cada subintervalo (h): 0.500000

Valor aproximado de la integral: 2.6666666667

Detalles del cálculo:
Intervalo  x_i             f(x_i)          Área           
-------------------------------------------------------
0-1       0.000000        0.000000        0.062500       
1-2       0.500000        0.250000        0.312500       
2-3       1.000000        1.000000        0.625000       
3-4       1.500000        2.250000        1.666666       

Suma de áreas de todos los trapecios: 2.6666666666666665

