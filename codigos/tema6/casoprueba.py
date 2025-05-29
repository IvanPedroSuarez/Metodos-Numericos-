import numpy as np

Vin = 0.0        # Voltaje de entrada (descarga)
R = 1e3          # Resistencia (ohms)
C = 100e-6       # Capacitancia (faradios)
V0 = 5.0         # Voltaje inicial (V)
h = 1.0          # Paso de tiempo (¡demasiado grande!)
t0 = 0.0
pasos = 5        # Simulamos 5 segundos

f = lambda t, V: (Vin - V)/(R*C)

def euler(f, t0, y0, h, n):
    t = [t0]
    y = [y0]
    for _ in range(n):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

t, V = euler(f, t0, V0, h, pasos)

for ti, Vi in zip(t, V):
    print(f"t={ti:.1f} s  -->  V={Vi:.3f} V")


output

t=0.0 s  -->  V=5.000 V
t=1.0 s  -->  V=-45.000 V
t=2.0 s  -->  V=445.000 V
t=3.0 s  -->  V=-4445.000 V
t=4.0 s  -->  V=44445.000 V
t=5.0 s  -->  V=-444445.000 V


# El método de Euler, al usar un paso tan grande, no captura la rápida caída exponencial del voltaje 
# y en vez de acercarse a cero, la solución alterna entre valores positivos y negativos cada vez más grandes (inestabilidad numérica)
