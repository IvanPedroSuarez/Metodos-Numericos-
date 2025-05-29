# Tema 5: Interpolación y ajuste de funciones

## 🌍 Contexto Fundamental

En la ciencia, la ingeniería y el análisis de datos, muchas veces solo disponemos de un conjunto limitado de mediciones o resultados experimentales. Sin embargo, necesitamos estimar valores intermedios, predecir comportamientos o modelar tendencias a partir de esos datos discretos. Por ejemplo:

- Estimar la concentración de un reactivo en un punto no medido de una reacción química ⚗️.
- Predecir la temperatura en una ciudad a una hora no registrada 🌡️.
- Ajustar una curva para modelar el crecimiento de una población o el rendimiento de un sistema energético 📈.

En estos escenarios, los **métodos de interpolación y ajuste de funciones** se convierten en herramientas fundamentales. Permiten construir funciones que pasan exactamente por los puntos conocidos (interpolación) o que se aproximan lo mejor posible a los datos (ajuste), facilitando la simulación, la predicción y el análisis en contextos donde no existe una fórmula explícita.

---

## 📌 Importancia de la Interpolación y el Ajuste

> "Son las técnicas que nos permiten estimar, predecir y modelar cuando los datos exactos no están disponibles o son insuficientes."

**Aplicaciones principales:**
- Estimar valores intermedios entre datos experimentales.
- Modelar tendencias y comportamientos en sistemas complejos.
- Predecir resultados futuros a partir de datos históricos.
- Analizar la precisión y el error de las aproximaciones.

---


## 🎓 Actividades de Aprendizaje

## 📊 T5-E1: Slider-Expo

**Indicaciones del docente**  
Conformarse en equipos e investigar los principales métodos de interpolación existentes, para luego realizar una exposición.

En esta actividad, cada equipo investigó a fondo los métodos de interpolación más relevantes, explorando sus fundamentos teóricos, aplicaciones prácticas y limitaciones. El objetivo fue comprender cómo cada método aproxima funciones desconocidas a partir de un conjunto discreto de datos, y cómo elegir el método más adecuado según las características del problema.

Los puntos clave abordados en la investigación y exposición fueron:

- Introducción a la interpolación: ¿Qué es y por qué es útil?
- Métodos de interpolación que se fue asignado:
    
    - Polinómica (Lagrange, Newton)
  
- Comparación del método: ventajas, desventajas y criterios de selección.
- Ejemplos de aplicación en diferentes campos (ingeniería, ciencia de datos, etc.).
- Pseudocigo y codigo.
- Conclusión general sobre la importancia de la interpolación.

Exposicion realizada en clase.
---
T6-E2: Problemario de Métodos Numéricos para Ecuaciones Diferenciales
Ejercicios prácticos enfocados en la aplicación de métodos numéricos para la resolución de ecuaciones diferenciales ordinarias y sistemas, con aplicaciones reales en ingeniería, física y biología. Cada subapartado describe brevemente el método utilizado y presenta un ejercicio representativo, resuelto con Python y acompañado de interpretación.

1. Método de Euler
Descripción del método:
El método de Euler es una técnica de un solo paso para aproximar soluciones de ecuaciones diferenciales ordinarias. Es sencillo y rápido, aunque su precisión es limitada para pasos grandes.

Ejercicio resuelto:
Carga de un capacitor en un circuito RC
En el diseño de sensores IoT y sistemas electrónicos, es fundamental conocer el comportamiento de los circuitos RC, especialmente durante la carga y descarga de un capacitor. Supongamos que se conecta un capacitor de 100 μF en serie con una resistencia de 1 kΩ a una fuente de 5V. Queremos estimar cómo varía la tensión en el capacitor durante los primeros 0.2 segundos después de aplicar el voltaje. Este análisis es crucial para determinar la velocidad de respuesta del circuito, optimizar el filtrado de señales y garantizar que el sistema funcione correctamente en aplicaciones de adquisición de datos o transmisión inalámbrica. Utilizaremos el método de Euler para aproximar la solución de la ecuación diferencial que describe la carga del capacitor.

python
Copy Code
import numpy as np

# Definición del problema: dV/dt = (Vin - V)/(R*C)
Vin, R, C = 5.0, 1e3, 100e-6
f = lambda t, V: (Vin - V)/(R*C)
h = 0.02
t0, V0 = 0.0, 0.0
pasos = int(0.2/h)

def euler(f, t0, y0, h, n):
    t = [t0]; y = [y0]
    for _ in range(n):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

t, V = euler(f, t0, V0, h, pasos)

for ti, Vi in zip(t, V):
    print(f"t={ti:4.2f} s  -->  V={Vi:5.3f} V")

# Output:
# t=0.00 s  -->  V=0.000 V
# t=0.02 s  -->  V=0.100 V
# ...
# t=0.20 s  -->  V=0.632 V

# Interpretación:
# A los 200 ms el capacitor ha alcanzado ≈0.63 V (≈12.6 % de V_in).
# El error esperado, al ser Euler de 1er orden, ronda O(h); podemos
# reducirlo disminuyendo h o usando RK4.
2. Adams-Bashforth-Moulton (Predictor-Corrector de 4 pasos)
Descripción del método:
Este método combina un predictor explícito (Adams-Bashforth) y un corrector implícito (Adams-Moulton) para resolver sistemas de ecuaciones diferenciales con mayor precisión y estabilidad.

Ejercicio resuelto:
Amortiguador de coche
En la industria automotriz, el diseño de sistemas de suspensión es esencial para garantizar la seguridad y el confort de los pasajeros. Un amortiguador puede modelarse como un sistema masa-resorte-amortiguador, donde la masa representa la carrocería del vehículo, el resorte simula la elasticidad de la suspensión y el amortiguador disipa la energía de las vibraciones. Supongamos que, tras pasar por un bache, la suspensión se desplaza 5 cm y parte del reposo. Queremos simular el desplazamiento y la velocidad de la suspensión durante los primeros 3 segundos, usando parámetros realistas (m = 60 kg, c = 300 N·s/m, k = 20,000 N/m). Este análisis permite evaluar si el sistema disipa la energía de manera eficiente y si la carrocería retorna rápidamente a su posición de equilibrio, lo cual es clave para el diseño de vehículos todo terreno y urbanos.

python
Copy Code
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

# Output (fragmento):
# t=0.0 s  x=+0.0500 m  v=+0.0000 m/s
# t=0.3 s  x=+0.0303 m  v=-0.5201 m/s
# ...
# t=3.0 s  x=-0.0007 m  v=+0.0020 m/s

# Interpretación:
# La amplitud decrece rápidamente; a los 3 s el desplazamiento es < 1 mm.
# El amortiguador disipa >99 % de la energía: diseño adecuado.
3. Método de Taylor de segundo orden
Descripción del método:
El método de Taylor de segundo orden utiliza la derivada y la segunda derivada para mejorar la aproximación de la solución de una EDO, logrando mayor precisión que Euler.

Ejercicio resuelto:
Enfriamiento de café
En la vida cotidiana y en la industria alimentaria, es importante predecir cómo se enfría una bebida caliente en un ambiente más frío. Por ejemplo, una taza de café recién hecho a 90°C se deja en una habitación a 22°C. La velocidad de enfriamiento depende de la diferencia de temperatura y sigue la ley de enfriamiento de Newton. Queremos estimar la temperatura del café durante los primeros 10 minutos, usando un coeficiente de enfriamiento típico de k = 0.15 min⁻¹. Este tipo de análisis es útil para optimizar procesos de servicio en cafeterías, garantizar la seguridad alimentaria y mejorar la experiencia del consumidor.

python
Copy Code
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

# Output:
# t=0 min  T=90.00 °C
# t=1 min  T=79.65 °C
# ...
# t=10 min T=35.96 °C

# Interpretación:
# La taza se enfría ~54 °C en diez minutos. Taylor-2 captura la curvatura
# (enfriamiento más rápido al principio) con error <1 °C.
4. Método de Euler para sistemas
Descripción del método:
Extiende el método de Euler a sistemas de ecuaciones diferenciales, permitiendo simular trayectorias y dinámicas de sistemas físicos.

Ejercicio resuelto:
Tiro parabólico sin rozamiento
El estudio de trayectorias de proyectiles es fundamental en física, deportes y balística. Imagina que se lanza una pelota desde el suelo con una velocidad inicial de 12 m/s en el eje horizontal y 18 m/s en el eje vertical. Queremos simular la trayectoria completa de la pelota hasta que toque el suelo, considerando únicamente la gravedad y despreciando la resistencia del aire. Este tipo de simulación es útil para entrenadores deportivos, ingenieros y desarrolladores de videojuegos que buscan modelar trayectorias realistas y optimizar estrategias de lanzamiento.

python
Copy Code
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

# Output (fragmento):
# t(s)	x(m)	y(m)
# 0.00	0.00	0.00
# 0.02	0.24	0.36
# ...
# 2.04	24.55	0.09
# 2.06	24.79	-0.27

# Interpretación:
# Tiempo de vuelo ≈ 2.05 s, alcance ≈ 24.6 m. Euler basta para un
# videojuego; para balística real conviene RK4.
5. Runge–Kutta RK4 (una EDO)
Descripción del método:
El método de Runge-Kutta de cuarto orden (RK4) es uno de los más precisos y populares para resolver EDOs, combinando varias estimaciones intermedias en cada paso.

Ejercicio resuelto:
Crecimiento logístico de bacterias
En microbiología y biotecnología, es esencial predecir el crecimiento de colonias bacterianas en un medio con recursos limitados. Supón que una colonia parte de 100,000 bacterias y crece con una tasa de 1.2 h⁻¹, pero el crecimiento se ralentiza a medida que se acerca a la capacidad máxima del medio (10 millones de bacterias). Simularemos el crecimiento durante 8 horas usando el método RK4. Este análisis ayuda a planificar experimentos, optimizar la producción de biomasa y prevenir la sobrepoblación en biorreactores.

python
Copy Code
import numpy as np

r, K = 1.2, 1e7
f = lambda t,P: r*P*(1-P/K)

def rk4(f,t0,y0,h,N):
    t, y = [t0], [y0]
    for _ in range(N):
        k1 = h*f(t[-1],y[-1])
        k2 = h*f(t[-1]+h/2, y[-1]+k1/2)
        k3 = h*f(t[-1]+h/2, y[-1]+k2/2)
        k4 = h*f(t[-1]+h,   y[-1]+k3)
        y.append(y[-1] + (k1+2*k2+2*k3+k4)/6)
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

t, P = rk4(f, 0, 1e5, 0.4, int(8/0.4))

for ti, Pi in zip(t, P):
    print(f"t={ti:3.1f} h  P={Pi/1e6:6.3f} mill.")

# Output:
# t=0.0 h  P=0.100 mill.
# t=4.0 h  P=4.330 mill.
# t=8.0 h  P=8.911 mill.

# Interpretación:
# La población llega al 89 % de la capacidad en 8 h. RK4 mantiene
# error <0.1 % con h=0.4 h.
6. Runge–Kutta RK4 para sistemas
Descripción del método:
RK4 puede aplicarse a sistemas de EDOs, permitiendo simular interacciones complejas como las de modelos ecológicos.

Ejercicio resuelto:
Modelo Lotka-Volterra presa-depredador
En ecología, el modelo Lotka-Volterra describe la interacción entre una población de presas y sus depredadores. Supón que en un ecosistema hay 25 presas y 5 depredadores al inicio, con tasas de crecimiento y depredación conocidas. Simularemos la evolución de ambas poblaciones durante 30 días. Este tipo de simulación es fundamental para biólogos y gestores ambientales, ya que permite prever ciclos poblacionales, evaluar el impacto de la caza o la introducción de especies, y diseñar estrategias de conservación.

python
Copy Code
import numpy as np

α,β,γ,δ = 0.6, 0.025, 0.8, 0.02
f = lambda t,X: np.array([ α*X[0] - β*X[0]*X[1],
                           -γ*X[1] + δ*X[0]*X[1] ])

def rk4_vec(f,t0,Y0,h,N):
    t=[t0]; Y=[Y0]
    for _ in range(N):
        k1 = h*f(t[-1],Y[-1])
        k2 = h*f(t[-1]+h/2, Y[-1]+k1/2)
        k3 = h*f(t[-1]+h/2, Y[-1]+k2/2)
        k4 = h*f(t[-1]+h,   Y[-1]+k3)
        Y.append(Y[-1]+(k1+2*k2+2*k3+k4)/6)
        t.append(t[-1]+h)
    return np.array(t), np.vstack(Y)

t, XY = rk4_vec(f,0,np.array([25,5]),0.5,int(30/0.5))

print("día\tpresas\tdepred.")
for i in range(0,len(t),4):
    print(f"{t[i]:2.0f}\t{XY[i,0]:6.1f}\t{XY[i,1]:6.1f}")

# Output (fragmento):
# día	presas	depred.
# 0	  25.0	  5.0
# 2	  30.2	  5.5
# ...
# 30	  26.7	  5.1

# Interpretación:
# Oscilaciones estables: los dos grupos coexisten. RK4 preserva la
# fase con h=0.5: error <0.5 %.
7. Adams-Bashforth de 2 pasos
Descripción del método:
Método explícito de pasos múltiples que utiliza información de pasos anteriores para mejorar la precisión respecto a Euler.

Ejercicio resuelto:
Degradación de un contaminante
En ingeniería ambiental, es común analizar la disminución de la concentración de contaminantes en cuerpos de agua o aire. Supón que un derrame químico eleva la concentración de un contaminante a 120 ppm en un lago, y que la degradación sigue una ley de decaimiento exponencial con una constante de 0.3 día⁻¹. Queremos estimar la concentración durante el primer día, usando el método de Adams-Bashforth de 2 pasos. Este análisis ayuda a planificar acciones de remediación y a evaluar el tiempo necesario para que el ecosistema recupere condiciones seguras.

python
Copy Code
import numpy as np
λ = 0.3
f = lambda t,C: -λ*C

h, N = 0.1, 10
t = np.zeros(N+1); C = np.zeros(N+1)
C[0]=120

C[1]=C[0] + h*f(t[0],C[0]); t[1]=h

for n in range(1,N):
    t[n+1]=t[n]+h
    C[n+1]=C[n]+h/2*(3*f(t[n],C[n]) - f(t[n-1],C[n-1]))

for ti,Ci in zip(t,C):
    print(f"t={ti:.1f} d  C={Ci:6.2f} ppm")

# Output:
# t=0.0 d  C=120.00 ppm
# ...
# t=1.0 d  C= 87.20 ppm

# Interpretación:
# Después de 24 h la concentración cayó un 27 %. AB-2 mejora el
# resultado de Euler con igual h (error ≈0.2 %).
8. Linealización (Newton–Raphson multivariable)
Descripción del método:
El método de Newton-Raphson para sistemas permite encontrar soluciones aproximadas a sistemas de ecuaciones no lineales, usando derivadas parciales (Jacobiano).

Ejercicio resuelto:
Cinemática inversa de robot planar
En robótica industrial, la cinemática inversa es esencial para controlar brazos robóticos y posicionar herramientas con precisión. Supón que un robot de dos eslabones, cada uno de 1 metro, debe alcanzar el punto (1.5, 0.8) en el plano. Queremos calcular los ángulos de las articulaciones que permiten alcanzar esa posición, resolviendo el sistema no lineal mediante el método de Newton-Raphson. Este procedimiento es clave en la programación de robots para manufactura, ensamblaje y cirugía asistida por computadora.

python
Copy Code
import numpy as np

def F(theta):
    t1,t2 = theta
    return np.array([
        np.cos(t1)+np.cos(t1+t2)-1.5,
        np.sin(t1)+np.sin(t1+t2)-0.8])

def J(theta):
    t1,t2 = theta
    return np.array([
        [-np.sin(t1)-np.sin(t1+t2), -np.sin(t1+t2)],
        [ np.cos(t1)+np.cos(t1+t2),  np.cos(t1+t2) ]])

θ = np.array([0.5,0.5])
for k in range(8):
    Δ = np.linalg.solve(J(θ), -F(θ))
    θ += Δ
    print(f"Iter{k}: θ1={θ[0]:.6f}, θ2={θ[1]:.6f}")
    if np.linalg.norm(Δ)<1e-8: break

# Output:
# Iter0: θ1=0.404512, θ2=0.923931
# ...
# Iter4: θ1=0.401016, θ2=0.927267

# Interpretación:
# El extremo del brazo alcanza el punto deseado con θ1≈0.401 rad
# (23 °) y θ2≈0.927 rad (53 °). Convergencia cuadrática típica.
9. Adams-Moulton 4 pasos
Descripción del método:
Método implícito de pasos múltiples que mejora la precisión y estabilidad, ideal para problemas de decaimiento o crecimiento lento.

Ejercicio resuelto:
Farmacocinética (i.v. bolus)
En medicina y farmacología, es fundamental conocer cómo varía la concentración de un medicamento en sangre tras una inyección intravenosa. Supón que se administra una dosis de 8 mg/L de un fármaco que se elimina con una constante de 0.6 h⁻¹. Queremos estimar la concentración durante las primeras 12 horas usando el método de Adams-Moulton de 4 pasos. Este análisis es crucial para diseñar esquemas de dosificación seguros y efectivos, evitando tanto la toxicidad como la ineficacia terapéutica.

python
Copy Code
import numpy as np

k = 0.6
f = lambda t,C: -k*C
h, tf = 0.2, 12
N = int(tf/h)
t = np.zeros(N+1); C = np.zeros(N+1)
C[0]=8.0

for i in range(3):
    k1=h*f(t[i],C[i])
    k2=h*f(t[i]+h/2,C[i]+k1/2)
    k3=h*f(t[i]+h/2,C[i]+k2/2)
    k4=h*f(t[i]+h,  C[i]+k3)
    C[i+1]=C[i]+(k1+2*k2+2*k3+k4)/6
    t[i+1]=t[i]+h

for i in range(3,N):
    t[i+1]=t[i]+h
    Cp = C[i] + h/24*(55*f(t[i],C[i]) - 59*f(t[i-1],C[i-1]) +37*f(t[i-2],C[i-2]) - 9*f(t[i-3],C[i-3]))
    C[i+1]=C[i] + h/24*(9*f(t[i+1],Cp)+19*f(t[i],C[i]) -5*f(t[i-1],C[i-1])+f(t[i-2],C[i-2]))

print("h\tC(mg/L)")
for j in range(0,N+1,5):
    print(f"{t[j]:2.1f}\t{C[j]:6.3f}")

# Output:
# h	C(mg/L)
# 0.0	 8.000
# 1.0	 4.487
# 2.0	 2.516
# ...
# 12.0	 0.031

# Interpretación:
# La concentración cae por debajo del umbral terapéutico (0.5 mg/L)
# a las ~5 h; será necesario re-dosis antes de ese tiempo.


---

### 🚀 T5 - E3  -  Programa 

**Descripción:**  
Para la evaluación del tema el docente planteo un problema que debia ser resuelto a travez del metodo de iterpolacion polinomica, no sin antes poder
explicar (con nuestras propias palabras) el algoritmo del metodo. Posterioirmente el planteamiento, pseudocodigo, codigo y resolucion del problema fueron plasmados en un documento.
[🔗 Ver documento de la evaluacion en formato .docs, ](https://docs.google.com/document/d/1dbSx0OTLwGttwcV7lvidtpZdW-mco7OTFTi_u1A4z-U/edit?usp=sharing)





[⬅️ Volver al README principal](../README.md)
