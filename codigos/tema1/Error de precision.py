#Error de precision

suma = 0.0
for i in range(1000000):
    suma += 0.000001

print("Suma obtenida:", suma)
print("Suma esperada:", 10**7 * 0.000001)

print(suma)


#Resultado al ejecutar en consola 
Ejemplo 1 de error de precisión en Python  
Suma obtenida: 1.0000000000007918  
Suma esperada: 1.0


      
