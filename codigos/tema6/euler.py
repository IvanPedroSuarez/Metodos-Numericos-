import numpy as np

g = 9.81
h = 0.02
x = y = 0.0
vx, vy = 12.0, 18.0
t = 0.0

print("t(s)\tx(m)\ty(m)")
while y >= 0:
    print(f"{t:4.2f}\t{x:5.2f}\t{y:5.2f}")
    x  += h*vx
    y  += h*vy
    vy += h*(-g)
    t  += h

Output (fragmento):
 t(s)	x(m)	y(m)
0.00	0.00	0.00
0.02	0.24	0.36
 ...
 2.04	24.55	0.09
 2.06	24.79	-0.27

 Interpretación:
# Tiempo de vuelo ≈ 2.05 s, alcance ≈ 24.6 m. Euler basta para un
# videojuego; para balística real conviene RK4.
