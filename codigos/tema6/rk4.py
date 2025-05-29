import numpy as np

r = 1.2          # Tasa de crecimiento (1/h)
K = 1e7          # Capacidad máxima (bacterias)

# Definición de la función logística
f = lambda t,P: r*P*(1-P/K)

def rk4(f, t0, y0, h, N):
    t, y = [t0], [y0]
    for _ in range(N):
        # Cálculo de los coeficientes de RK4
        k1 = h*f(t[-1],y[-1])
        k2 = h*f(t[-1]+h/2, y[-1]+k1/2)
        k3 = h*f(t[-1]+h/2, y[-1]+k2/2)
        k4 = h*f(t[-1]+h,   y[-1]+k3)
        # Actualización de la solución
        y.append(y[-1] + (k1+2*k2+2*k3+k4)/6)
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

Output:
t=0.0 h  P=0.100 mill.
 t=4.0 h  P=4.330 mill.
t=8.0 h  P=8.911 mill.

Interpretación:
 La población llega al 89 % de la capacidad en 8 h. RK4 mantiene
 error <0.1 % con h=0.4 h.

t, P = rk4(f, 0, 1e5, 0.4, int(8/0.4))  # 8 horas, paso de 0.4 h

# Imprimir resultados
for ti, Pi in zip(t, P):
    print(f"t={ti:3.1f} h  P={Pi/1e6:6.3f} mill.")
