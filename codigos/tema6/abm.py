iimport numpy as np

# Parámetros del circuito RC
Vin = 5.0        # Voltaje de entrada (V)
R = 1e3          # Resistencia (ohms)
C = 100e-6       # Capacitancia (faradios)

# Definición de la función diferencial: dV/dt = (Vin - V)/(R*C)
f = lambda t, V: (Vin - V)/(R*C)

h = 0.02         # Paso de tiempo (s)
t0 = 0.0         # Tiempo inicial (s)
V0 = 0.0         # Voltaje inicial en el capacitor (V)
pasos = int(0.2/h)  # Número de pasos para 0.2 segundos

def euler(f, t0, y0, h, n):
    t = [t0]
    y = [y0]
    for _ in range(n):
        # Método de Euler: y_{n+1} = y_n + h*f(t_n, y_n)
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

t, V = euler(f, t0, V0, h, pasos)

# Imprimir resultados
for ti, Vi in zip(t, V):
    print(f"t={ti:4.2f} s  -->  V={Vi:5.3f} V")



Output (fragmento):
t=0.0 s  x=+0.0500 m  v=+0.0000 m/s
t=0.3 s  x=+0.0303 m  v=-0.5201 m/s
 ...
t=3.0 s  x=-0.0007 m  v=+0.0020 m/s

 Interpretación:
 La amplitud decrece rápidamente; a los 3 s el desplazamiento es < 1 mm.
 El amortiguador disipa >99 % de la energía: diseño adecuado.
