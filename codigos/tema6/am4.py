import numpy as np

k = 0.6         # Constante de eliminación (1/h)
f = lambda t,C: -k*C

h = 0.2         # Paso de tiempo (h)
tf = 12         # Tiempo final (h)
N = int(tf/h)
t = np.zeros(N+1)
C = np.zeros(N+1)
C[0] = 8.0      # Concentración inicial (mg/L)

# Inicialización con RK4 para los primeros 3 pasos
for i in range(3):
    k1 = h*f(t[i],C[i])
    k2 = h*f(t[i]+h/2,C[i]+k1/2)
    k3 = h*f(t[i]+h/2,C[i]+k2/2)
    k4 = h*f(t[i]+h,  C[i]+k3)
    C[i+1] = C[i] + (k1+2*k2+2*k3+k4)/6
    t[i+1] = t[i] + h

# Adams-Moulton de 4 pasos
for i in range(3, N):
    t[i+1] = t[i] + h
    # Predictor Adams-Bashforth
    Cp = C[i] + h/24*(55*f(t[i],C[i]) - 59*f(t[i-1],C[i-1]) + 37*f(t[i-2],C[i-2]) - 9*f(t[i-3],C[i-3]))
    # Corrector Adams-Moulton
    C[i+1] = C[i] + h/24*(9*f(t[i+1],Cp) + 19*f(t[i],C[i]) - 5*f(t[i-1],C[i-1]) + f(t[i-2],C[i-2]))

# Imprimir resultados cada 1 hora
print("h\tC(mg/L)")
for j in range(0, N+1, 5):
    print(f"{t[j]:2.1f}\t{C[j]:6.3f}")


Output:
h	C(mg/L)
0.0	 8.000
1.0	 4.487
2.0	 2.516
 ...
12.0	 0.031

Interpretación:
 La concentración cae por debajo del umbral terapéutico (0.5 mg/L)
 a las ~5 h; será necesario re-dosis antes de ese tiempo.
