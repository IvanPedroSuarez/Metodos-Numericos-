##ERROR DE PRECISION - EJEMPLO EN PYTHON##

# Inicializamos la variable suma en 0
suma = 0
# Realizamos 10 iteraciones sumando 0.1 en cada una
# Este proceso debería dar 1.0, pero debido a la representación binaria de punto flotante
# puede haber pequeñas diferencias
for i in range(10):
    suma += 0.1

# Mostramos los resultados y calculamos los errores
print(f"Valor esperado: 1.0")
print(f"Valor obtenido: {suma}")
# Error absoluto: diferencia entre el valor obtenido y el esperado
print(f"Error absoluto: {abs(suma - 1.0)}")
# Error relativo: error absoluto dividido entre el valor real
print(f"Error relativo: {abs(suma - 1.0)/1.0}")


##Output 
1. ERROR DE PRECISIÓN
--------------------------------------------------
Valor esperado: 1.0
Valor obtenido: 0.9999999999999999
Error absoluto: 1.1102230246251565e-16
Error relativo: 1.1102230246251565e-16
# El resultado muestra que al sumar 0.1 diez veces:
# Valor esperado: 1.0
# Valor obtenido: 0.9999999999999999
# Error absoluto: 1.1102e-16 (muy pequeño pero existe)
# Este error ocurre por la representación binaria de decimales

