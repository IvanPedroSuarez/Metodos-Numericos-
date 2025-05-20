import numpy as np
from math import sin, cos, tan, exp, log, sqrt, pi
 
 
def simpson_13_interactivo():
	"""
	Programa interactivo para calcular integrales definidas usando la regla de Simpson 1/3.
	Versión corregida para manejar funciones con numpy.
 
	La regla de Simpson 1/3 aproxima la integral de una función mediante la interpolación
	cuadrática de la función en subintervalos consecutivos.
	"""
	# Mostrar encabezado y instrucciones para el usuario
	print("=== Calculadora de Integrales por Regla de Simpson 1/3 ===")
	print("\nInstrucciones:")
	print("1. Ingrese la función a integrar usando x como variable")
	print("2. Use funciones matemáticas como sin(), cos(), exp(), etc.")
	print("3. Ejemplos válidos: 'x**3 + 2*x', 'np.sin(x)*np.cos(x)', 'np.exp(-x**2)'")
	print("4. El número de subintervalos (n) debe ser par (si ingresa impar, se ajustará)")
 
	# SOLICITAR DATOS DE ENTRADA
	# --------------------------
	# Pedir al usuario la función a integrar y los parámetros de integración
	funcion_str = input("\nIngrese la función a integrar (en términos de x): ")
	a = float(input("Ingrese el límite inferior de integración (a): "))
	b = float(input("Ingrese el límite superior de integración (b): "))
	n = int(input("Ingrese el número de subintervalos (n > 0, preferiblemente par): "))
 
	# VALIDACIÓN DE ENTRADAS
	# ---------------------
	# Verificar que el número de subintervalos sea positivo
	if n <= 0:
    	print("\nError: El número de subintervalos debe ser positivo")
    	return
 
	# Ajustar n si es impar (el método requiere n par)
	if n % 2 != 0:
    	print(f"\nNota: Se ajustó n de {n} a {n + 1} (debe ser par para Simpson 1/3)")
    	n += 1
 
	# DEFINICIÓN DE LA FUNCIÓN A INTEGRAR
	# ----------------------------------
	# Convertir la cadena de entrada en una función evaluable
	def f(x):
    	"""
    	Función vectorizada que evalúa la expresión matemática ingresada por el usuario.
 
    	Args:
        	x: Valor o array de valores donde se evaluará la función
 
    	Returns:
        	Valor(es) de la función evaluada en x
    	"""
    	# Reemplazar funciones math por numpy para permitir operaciones vectorizadas
    	funcion_np = funcion_str.replace('sin', 'np.sin')
    	funcion_np = funcion_np.replace('cos', 'np.cos')
    	funcion_np = funcion_np.replace('tan', 'np.tan')
    	funcion_np = funcion_np.replace('exp', 'np.exp')
    	funcion_np = funcion_np.replace('log', 'np.log')
    	funcion_np = funcion_np.replace('sqrt', 'np.sqrt')
 
    	# Evaluar la expresión con numpy como np y x como variable
    	return eval(funcion_np, {'np': np, 'x': x})
 
	# CÁLCULO DE LA INTEGRAL
	# ----------------------
	try:
    	# Paso 1: Calcular el ancho de cada subintervalo
    	h = (b - a) / n
 
    	# Paso 2: Generar los puntos equidistantes en el intervalo [a, b]
    	x = np.linspace(a, b, n + 1)
 
    	# Paso 3: Evaluar la función en todos los puntos x
    	y = f(x)
 
    	# Paso 4: Inicializar la suma con los términos extremos (coeficiente 1)
    	suma = y[0] + y[-1]  # Primer y último término
 
    	# Paso 5: Sumar términos con coeficiente 4 (para puntos con índice impar)
    	for i in range(1, n, 2):
        	suma += 4 * y[i]
 
    	# Paso 6: Sumar términos con coeficiente 2 (para puntos con índice par)
    	for i in range(2, n - 1, 2):
        	suma += 2 * y[i]
 
    	# Paso 7: Calcular la integral aproximada según la fórmula de Simpson 1/3
    	integral = (h / 3) * suma
 
    	# PRESENTACIÓN DE RESULTADOS
    	# -------------------------
    	print("\n=== Resultados ===")
    	print(f"Función integrada: f(x) = {funcion_str}")
    	print(f"Límites de integración: [{a}, {b}]")
    	print(f"Número de subintervalos usado: {n}")
    	print(f"Ancho de cada subintervalo (h): {h:.6f}")
    	print(f"\nValor aproximado de la integral: {integral:.10f}")
 
    	# Mostrar tabla detallada solo para n pequeño (para no saturar la salida)
    	if n <= 10:
        	print("\nDetalles del cálculo:")
        	# Encabezado de la tabla
        	print(f"{'Punto':<8} {'x_i':<15} {'f(x_i)':<15} {'Coeficiente':<12} {'Contribución':<15}")
        	print("-" * 65)
 
        	# Primer punto (coeficiente 1)
        	contrib = y[0] * h / 3
        	print(f"{0:<8} {x[0]:<15.6f} {y[0]:<15.6f} {1:<12} {contrib:<15.6f}")
 
        	# Puntos intermedios (alternan coeficientes 4 y 2)
        	for i in range(1, n):
            	coef = 4 if i % 2 == 1 else 2  # Coef 4 para índices impares, 2 para pares
            	contrib = y[i] * coef * h / 3
            	print(f"{i:<8} {x[i]:<15.6f} {y[i]:<15.6f} {coef:<12} {contrib:<15.6f}")
 
        	# Último punto (coeficiente 1)
        	contrib = y[-1] * h / 3
        	print(f"{n:<8} {x[-1]:<15.6f} {y[-1]:<15.6f} {1:<12} {contrib:<15.6f}")
 
        	# Mostrar suma total
        	print("\nSuma ponderada de todas las contribuciones:", integral)
 
	# MANEJO DE ERRORES
	# ----------------
	except Exception as e:
    	print(f"\nError al calcular la integral: {str(e)}")
    	print("Posibles causas:")
    	print("- Función mal escrita (revise paréntesis y operadores)")
    	print("- Función no definida en algún punto del intervalo")
    	print("- Uso de variables distintas a 'x'")
 
 
# EJECUCIÓN DEL PROGRAMA
# ----------------------
if __name__ == "__main__":
	# Punto de entrada principal del programa
	simpson_13_interactivo()
