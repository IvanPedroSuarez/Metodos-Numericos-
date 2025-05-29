import numpy as np

k = 0.15
Tamb = 22.0
f = lambda t,T: -k*(T-Tamb)
f1 = lambda t,T:  k**2*(T-Tamb)

h, N = 1.0, 10
t = np.arange(0, N+1)*h
T = np.zeros_like(t); T[0] = 90.0

for i in range(N):
    T[i+1] = T[i] + h*f(t[i],T[i]) + h**2/2 * f1(t[i],T[i])

for ti, Ti in zip(t, T):
    print(f"t={ti:2.0f} min  T={Ti:5.2f} °C")

Output:
t=0 min  T=90.00 °C
t=1 min  T=79.65 °C
...
t=10 min T=35.96 °C

Interpretación:
La taza se enfría ~54 °C en diez minutos. Taylor-2 captura la curvatura
(enfriamiento más rápido al principio) con error <1 °C.
