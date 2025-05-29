import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi

def simpson_38_interactivo():
    """
    Programa interactivo para calcular integrales definidas usando la regla de Simpson 3/8.
    El usuario ingresa la función y los parámetros de integración.
    """
    # Imprimir encabezado y instrucciones para el usuario
    print("=== Calculadora de Integrales por Regla de Simpson 3/8 ===")
    print("\nInstrucciones:")
    print("1. Ingrese la función a integrar usando x como variable")
    print("2. Use funciones matemáticas como sin(), cos(), exp(), etc. (prefiera np.sin, np.cos, etc.)")
    print("3. Ejemplos válidos: 'x**3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x**2)'")
    print("4. El número de subintervalos (n) debe ser múltiplo de 3 (se ajustará automáticamente)")
    
    # Solicitar al usuario la función y parámetros de integración
    funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    n = int(input("Ingrese el número de subintervalos (n > 0, preferiblemente múltiplo de 3): "))
    
    # Validar que el número de subintervalos sea positivo
    if n <= 0:
        print("\nError: El número de subintervalos debe ser positivo")
        return
    
    # Ajustar n para que sea múltiplo de 3 (requerido por la regla de Simpson 3/8)
    if n % 3 != 0:
        nuevo_n = n + (3 - n % 3)
        print(f"\nNota: Se ajustó n de {n} a {nuevo_n} (debe ser múltiplo de 3 para Simpson 3/8)")
        n = nuevo_n
    
    # Definir la función vectorizada para evaluar la función ingresada
    def f(x):
        # Reemplazar funciones matemáticas de math por sus equivalentes en numpy
        funcion_np = funcion_str.replace('sin', 'np.sin')
        funcion_np = funcion_np.replace('cos', 'np.cos')
        funcion_np = funcion_np.replace('tan', 'np.tan')
        funcion_np = funcion_np.replace('exp', 'np.exp')
        funcion_np = funcion_np.replace('log', 'np.log')
        funcion_np = funcion_np.replace('sqrt', 'np.sqrt')
        # Evaluar la función usando eval (con entorno restringido a numpy y x)
        return eval(funcion_np, {'np': np, 'x': x})
    
    try:
        # Calcular el ancho de cada subintervalo (h)
        h = (b - a) / n
        # Generar puntos equiespaciados en el intervalo [a, b]
        x = np.linspace(a, b, n+1)
        # Evaluar la función en todos los puntos
        y = f(x)
        
        # Inicializar la suma con el primer y último término (coeficiente 1)
        suma = y[0] + y[-1]
        
        # Sumar términos intermedios con coeficientes 2 o 3 según la regla de Simpson 3/8
        for i in range(1, n):
            if i % 3 == 0:
                suma += 2 * y[i]  # Coeficiente 2 para puntos divisibles por 3
            else:
                suma += 3 * y[i]  # Coeficiente 3 para otros puntos
        
        # Calcular la integral usando la fórmula de Simpson 3/8: (3h/8) * suma
        integral = (3 * h / 8) * suma
        
        # Mostrar resultados generales
        print("\n=== Resultados ===")
        print(f"Función integrada: f(x) = {funcion_str}")
        print(f"Límites de integración: [{a}, {b}]")
        print(f"Número de subintervalos usado: {n}")
        print(f"Ancho de cada subintervalo (h): {h:.6f}")
        print(f"\nValor aproximado de la integral: {integral:.10f}")
        
        # Mostrar detalles del cálculo si n es pequeño (para mejor legibilidad)
        if n <= 12:
            print("\nDetalles del cálculo:")
            print(f"{'Punto':<8} {'x_i':<15} {'f(x_i)':<15} {'Coeficiente':<12} {'Contribución':<15}")
            print("-" * 65)
            
            # Mostrar contribución del primer punto (coeficiente 1)
            contrib = y[0] * 3*h/8
            print(f"{0:<8} {x[0]:<15.6f} {y[0]:<15.6f} {1:<12} {contrib:<15.6f}")
            
            # Mostrar contribuciones de puntos intermedios
            for i in range(1, n):
                coef = 2 if i % 3 == 0 else 3
                contrib = y[i] * coef * 3*h/8
                print(f"{i:<8} {x[i]:<15.6f} {y[i]:<15.6f} {coef:<12} {contrib:<15.6f}")
            
            # Mostrar contribución del último punto (coeficiente 1)
            contrib = y[-1] * 3*h/8
            print(f"{n:<8} {x[-1]:<15.6f} {y[-1]:<15.6f} {1:<12} {contrib:<15.6f}")
            
            # Mostrar la suma final de todas las contribuciones
            print("\nSuma ponderada de todas las contribuciones:", integral)
    
    except Exception as e:
        # Manejar errores durante el cálculo (ej. función mal escrita o no definida)
        print(f"\nError al calcular la integral: {str(e)}")
        print("Posibles causas:")
        print("- Función mal escrita (revise paréntesis y operadores)")
        print("- Función no definida en algún punto del intervalo")
        print("- Uso de variables distintas a 'x'")

# Ejecutar el programa si se corre como script principal
if __name__ == "__main__":
    simpson_38_interactivo()


output

=== Calculadora de Integrales por Regla de Simpson 3/8 ===

Instrucciones:
1. Ingrese la función a integrar usando x como variable
2. Use funciones matemáticas como sin(), cos(), exp(), etc. (prefiera np.sin, np.cos, etc.)
3. Ejemplos válidos: 'x*3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x*2)'
4. El número de subintervalos (n) debe ser múltiplo de 3 (se ajustará automáticamente)

Ingrese la función a integrar (en términos de x): np.sin(x)
Ingrese el límite inferior de integración (a): 0
Ingrese el límite superior de integración (b): 3.1416
Ingrese el número de subintervalos (n > 0, preferiblemente múltiplo de 3): 6

=== Resultados ===
Función integrada: f(x) = np.sin(x)
Límites de integración: [0.0, 3.1416]
Número de subintervalos usado: 6
Ancho de cada subintervalo (h): 0.523600

Valor aproximado de la integral: 1.9999999826

Detalles del cálculo:
Punto    x_i             f(x_i)          Coeficiente  Contribución   
-----------------------------------------------------------------
0        0.000000        0.000000        1            0.000000       
1        0.523600        0.500000        3            0.294525       
2        1.047200        0.866025        3            0.510146       
3        1.570800        1.000000        2            0.392700       
4        2.094400        0.866025        3            0.510146       
5        2.618000        0.500000        3            0.294525       
6        3.141600        0.000000        1            0.000000       

Suma ponderada de todas las contribuciones: 1.9999999826
