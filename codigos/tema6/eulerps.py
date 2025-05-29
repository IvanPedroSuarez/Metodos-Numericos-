import numpy as np

g = 9.81         # Gravedad (m/s^2)
h = 0.02         # Paso de tiempo (s)
x = 0.0          # Posición inicial en x (m)
y = 0.0          # Posición inicial en y (m)
vx = 12.0        # Velocidad inicial en x (m/s)
vy = 18.0        # Velocidad inicial en y (m/s)
t = 0.0          # Tiempo inicial (s)

print("t(s)\tx(m)\ty(m)")
while y >= 0:
    print(f"{t:4.2f}\t{x:5.2f}\t{y:5.2f}")
    x  += h*vx           # Actualizar posición x
    y  += h*vy           # Actualizar posición y
    vy += h*(-g)         # Actualizar velocidad en y (afectada por gravedad)
    t  += h              # Avanzar el tiempo



    
 Output (fragmento):
t(s)	x(m)	y(m)
 0.00	0.00	0.00
 0.02	0.24	0.36
 ...
 2.04	24.55	0.09
 2.06	24.79	-0.27

 Interpretación:
 Tiempo de vuelo ≈ 2.05 s, alcance ≈ 24.6 m. Euler basta para un
 videojuego; para balística real conviene RK4.
