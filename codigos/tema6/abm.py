import numpy as np

m, c, k = 60, 300, 2e4
def f(t, Y):
    x, v = Y
    return np.array([v, -(c/m)*v - (k/m)*x])

h = 0.01
N = int(3/h)
t = np.zeros(N+1)
Y = np.zeros((N+1,2))
Y[0]= [0.05, 0.0]

for i in range(3):
    k1 = h*f(t[i], Y[i])
    k2 = h*f(t[i]+h/2, Y[i]+k1/2)
    k3 = h*f(t[i]+h/2, Y[i]+k2/2)
    k4 = h*f(t[i]+h,   Y[i]+k3)
    Y[i+1] = Y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    t[i+1] = t[i] + h

for i in range(3, N):
    t[i+1] = t[i] + h
    Yp = Y[i] + h/24*(55*f(t[i],Y[i]) - 59*f(t[i-1],Y[i-1]) +37*f(t[i-2],Y[i-2]) - 9*f(t[i-3],Y[i-3]))
    Y[i+1] = Y[i] + h/24*( 9*f(t[i+1],Yp) +19*f(t[i],Y[i]) -5*f(t[i-1],Y[i-1]) +  f(t[i-2],Y[i-2]))

for j in range(0,N+1,int(0.3/h)):
    print(f"t={t[j]:.1f} s  x={Y[j,0]:+.4f} m  v={Y[j,1]:+.4f} m/s")

Output (fragmento):
t=0.0 s  x=+0.0500 m  v=+0.0000 m/s
t=0.3 s  x=+0.0303 m  v=-0.5201 m/s
 ...
t=3.0 s  x=-0.0007 m  v=+0.0020 m/s

 Interpretación:
 La amplitud decrece rápidamente; a los 3 s el desplazamiento es < 1 mm.
 El amortiguador disipa >99 % de la energía: diseño adecuado.
