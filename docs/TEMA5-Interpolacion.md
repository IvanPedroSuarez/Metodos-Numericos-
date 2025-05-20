# Tema 2: Métodos de Solución de Ecuaciones No Lineales

## 🌍 Contexto Fundamental

En el mundo real, los problemas científicos y de ingeniería rara vez se presentan en formas simples o con soluciones exactas. Muchas veces, nos enfrentamos a **ecuaciones no lineales** que no pueden resolverse de manera directa mediante técnicas algebraicas tradicionales. Por ejemplo:

- Calcular la trayectoria precisa de un satélite 🛰️, donde la resistencia del aire y la gravedad varían con la altitud.
- Determinar los puntos de equilibrio en reacciones químicas ⚗️, donde las ecuaciones de estado son altamente no lineales.
- Optimizar el rendimiento de sistemas energéticos 🔋, donde intervienen múltiples variables interdependientes.

En estos escenarios, los **métodos numéricos** se convierten en herramientas esenciales. Permiten aproximar soluciones con la precisión deseada, utilizando algoritmos iterativos que pueden implementarse fácilmente en una computadora. Así, los métodos numéricos actúan como el puente entre la teoría matemática y la resolución práctica de problemas complejos, abriendo la puerta a la simulación, el modelado y la optimización en la ciencia y la ingeniería moderna.

---

## 📌 Importancia de los Métodos de Solución

> "Son las herramientas que nos permiten encontrar respuestas donde las matemáticas tradicionales se quedan cortas."

**Aplicaciones principales:**
- Encontrar raíces de ecuaciones no lineales.
- Optimización de funciones complejas.
- Resolución de sistemas de ecuaciones.
- Análisis de convergencia y error.

---

## 🎓 Actividades de Aprendizaje

### 📊 T2-E1: Exposición de Métodos Numéricos

**Indicaciones del docente**  
Conformarse en equipo e investigar los diferentes métodos de solución para una ecuación ( bisección , regla falta, interpolación, secante , etc), y entregar un reporte o tabla comparativa.

El metodo asignado fue el de la secante (actividad realizada en equipo), donde se abaracaron los siguientes puntos 


- Introducción del metodo
- ¿Qué es?
- Fórmula
- Pasos para aplicar el método
- Requisitos para aplicar el método
- Ejemplo (video)
- Aplicaciones
- Ventajas y Desventajas
- Errores
- Tabla comparativa
- Desafío
- Conclusión General.

[🔗 Ver presentacion sobre el metodo de la secante (Canva)](https://www.canva.com/design/DAGe18Zxr5k/NBIKlX_VZRux4u_mbS9y4A/edit?utm_content=DAGe18Zxr5k&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---


## 💻 T2-E2: Problemario de Métodos de Solución

Ejercicios prácticos enfocados en la aplicación de los métodos numéricos para interpolación, regresión, correlación y mínimos cuadrados. Cada subapartado describe brevemente el método utilizado y presenta un ejercicio representativo, resuelto con Python.

---

### 1. Interpolación Lineal

**Descripción del método:**  
La interpolación lineal estima el valor de una función entre dos puntos conocidos, asumiendo que el cambio entre ellos es lineal. Es simple y útil cuando los datos son aproximadamente rectos entre los puntos.

**Ejercicio resuelto:**  
Aproximar el valor de \( f(x) = \sqrt{x} \) en \( x = 6 \) usando los puntos conocidos \( (1, 1.0), (4, 2.0), (9, 3.0) \).

[🔗 Ver código de interpolación lineal (Python)](./codigo/interpolacion_lineal.py)

---

### 2. Interpolación Polinómica (Lagrange)

**Descripción del método:**  
La interpolación polinómica de Lagrange construye un polinomio que pasa exactamente por todos los puntos conocidos. Es útil para estimar valores intermedios, pero puede ser inestable si se usan muchos puntos.

**Ejercicio resuelto:**  
Aproximar el valor de \( f(x) = x^2 \) en \( x = 3 \) usando los puntos \( (1, 1), (2, 4), (4, 16) \).

[🔗 Ver código de interpolación polinómica (Python)](./codigo/interpolacion_polinomica.py)

---

### 3. Regresión Lineal

**Descripción del método:**  
La regresión lineal ajusta una recta a un conjunto de datos, minimizando la suma de los errores cuadrados. Es útil para modelar tendencias generales cuando los datos presentan ruido.

**Ejercicio resuelto:**  
Ajustar una recta a los datos de temperatura en función de la hora:  
Horas: [8, 12, 14, 16]  
Temperaturas: [15, 22, 25, 24]

[🔗 Ver código de regresión lineal (Python)](./codigo/regresion_lineal.py)

---

### 4. Correlación

**Descripción del método:**  
El coeficiente de correlación de Pearson mide la fuerza y dirección de la relación lineal entre dos variables. Un valor de 1 indica correlación positiva perfecta, -1 negativa perfecta y 0 ausencia de correlación lineal.

**Ejercicio resuelto:**  
Calcular el coeficiente de correlación para los datos:  
x: [1, 2, 3, 4, 5]  
y: [2, 4, 6, 8, 10]

[🔗 Ver código de correlación (Python)](./codigo/correlacion.py)

---

### 5. Mínimos Cuadrados

**Descripción del método:**  
El método de mínimos cuadrados ajusta una recta a los datos minimizando el error cuadrático medio. Es ampliamente usado para predicción y análisis de tendencias.

**Ejercicio resuelto:**  
Ajustar una recta a los datos:  
x: [1, 2, 3, 4, 5]  
y: [2.1, 3.9, 6.2, 7.8, 10.3]  
y estimar el valor para \( x = 6 \).

[🔗 Ver código de mínimos cuadrados (Python)](./codigo/minimos_cuadrados.py)

---

Cada ejercicio incluye el análisis del procedimiento, la interpretación de resultados y la discusión de posibles dificultades o casos especiales.

---


[⬅️ Volver al README principal](../README.md)

