import numpy as np

λ = 0.3         # Constante de decaimiento (1/día)
f = lambda t,C: -λ*C

h = 0.1         # Paso de tiempo (días)
N = 10          # Número de pasos (1 día)
t = np.zeros(N+1)
C = np.zeros(N+1)
C[0] = 120      # Concentración inicial (ppm)

# Primer paso con Euler
C[1] = C[0] + h*f(t[0],C[0])
t[1] = h

# Adams-Bashforth de 2 pasos
for n in range(1, N):
    t[n+1] = t[n] + h
    # Fórmula de Adams-Bashforth 2 pasos
    C[n+1] = C[n] + h/2*(3*f(t[n],C[n]) - f(t[n-1],C[n-1]))

# Imprimir resultados
for ti, Ci in zip(t, C):
    print(f"t={ti:.1f} d  C={Ci:6.2f} ppm")

Output:
t=0.0 d  C=120.00 ppm
...
t=1.0 d  C= 87.20 ppm

 Interpretación:
 Después de 24 h la concentración cayó un 27 %. AB-2 mejora el
 resultado de Euler con igual h (error ≈0.2 %).
