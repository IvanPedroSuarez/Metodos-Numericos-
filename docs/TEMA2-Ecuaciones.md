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

**Objetivo:**  
Presentar y comparar los diferentes métodos numéricos para la solución de ecuaciones no lineales, destacando sus fundamentos, ventajas, limitaciones y aplicaciones prácticas.

**Incluye:**
- Análisis comparativo de métodos.
- Ejemplos prácticos de aplicación.
- Demostraciones de implementación en Python.
- Discusión de ventajas y limitaciones.

---

### 💻 T2-E2: Problemario de Métodos de Solución

**Descripción:**  
Ejercicios prácticos enfocados en la aplicación de los métodos numéricos para encontrar raíces de ecuaciones no lineales. Cada subapartado describe brevemente el método utilizado y presenta un ejercicio representativo, resuelto con Python.

---

#### 1. Método de Bisección

**Descripción del método:**  
El método de bisección es un procedimiento iterativo que consiste en dividir repetidamente un intervalo en dos mitades y seleccionar la subintervalo donde ocurre un cambio de signo, garantizando así la existencia de una raíz. Es un método robusto y siempre converge si la función es continua y hay cambio de signo.

**Ejercicio resuelto:**  
Aproximar la raíz de la función \( f(x) = x^3 - 25 \) en el intervalo \([1, 3]\).

**Procedimiento:**  
Se seleccionan los extremos del intervalo, se verifica el cambio de signo, se calcula el punto medio y se repite el proceso hasta alcanzar la precisión deseada.

**Resultado:**  
Después de varias iteraciones, se obtiene una raíz aproximada en \( x \approx 2.924 \).

[🔗 Ver código de método de bisección (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20biseccion.py)

---

#### 2. Método de la Regla Falsa

**Descripción del método:**  
La regla falsa, o método de falsa posición, es similar a la bisección pero utiliza una aproximación lineal entre los extremos del intervalo para estimar la raíz. Es más rápido que la bisección en muchos casos, aunque puede estancarse si la función es muy asimétrica.

**Ejercicio resuelto:**  
Encontrar la raíz de \( f(x) = x^3 - x - 1 \) en el intervalo \([1, 2]\).

**Procedimiento:**  
Se usan los extremos del intervalo y la fórmula de la regla falsa para aproximar la raíz, actualizando el intervalo en cada iteración.

**Resultado:**  
El método converge a una raíz aproximada dentro del intervalo.

[🔗 Ver código de método de regla falsa (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20regla%20falsa.py)

---

#### 3. Método de Punto Fijo

**Descripción del método:**  
El método de punto fijo transforma la ecuación original en una forma iterativa \( x = g(x) \) y utiliza una suposición inicial para generar una sucesión que converge a la raíz, siempre que la función de iteración cumpla ciertas condiciones de convergencia.

**Ejercicio resuelto:**  
Resolver \( f(x) = e^{-x} - x \) usando la función de iteración \( x = e^{-x} \).

**Procedimiento:**  
Se elige un valor inicial y se itera usando la función de punto fijo hasta que el error absoluto sea suficientemente pequeño.

**Resultado:**  
La raíz se aproxima a \( x \approx 0.5671 \).

[🔗 Ver código de método de punto fijo (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20punto%20fijo.py)

---

#### 4. Método de Newton-Raphson

**Descripción del método:**  
El método de Newton-Raphson utiliza la derivada de la función para construir una sucesión que converge rápidamente a la raíz, partiendo de una suposición inicial. Es muy eficiente, pero requiere que la derivada no sea cero y que la suposición inicial esté cerca de la raíz.

**Ejercicio resuelto:**  
Determinar la raíz de \( f(x) = x^3 - x - 1 \) usando un valor inicial \( x_0 = 1.5 \).

**Procedimiento:**  
Se calcula la derivada, se aplica la fórmula de Newton-Raphson y se repite hasta alcanzar la tolerancia deseada.

**Resultado:**  
El método converge rápidamente a la raíz real de la función.

[🔗 Ver código de método de Newton-Raphson (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20newton-raphson.py)

---

#### 5. Método de la Secante

**Descripción del método:**  
El método de la secante es una variante del método de Newton-Raphson que no requiere el cálculo de la derivada. Utiliza dos aproximaciones iniciales y construye una sucesión usando una secante entre los puntos.

**Ejercicio resuelto:**  
Encontrar la raíz de \( f(x) = \cos(x) - x \) usando valores iniciales \( x_0 = 0.5 \) y \( x_1 = 1 \).

**Procedimiento:**  
Se aplica la fórmula de la secante iterativamente hasta que el error relativo sea suficientemente pequeño.

**Resultado:**  
La raíz se aproxima a \( x \approx 0.739 \).

[🔗 Ver código de método de la secante (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20la%20secante.py)

---

Cada ejercicio incluye el análisis del procedimiento, la interpretación de resultados y la discusión de posibles dificultades o casos especiales.  
[🔗 Ver todos los códigos de implementación](https://github.com/IvanPedroSuarez/Metodos-Numericos-/tree/master/codigos/tema2)

---

### 🚀 T2-E3: Proyecto Integrador

**Descripción:**  
Desarrollo de una aplicación que implemente múltiples métodos de solución de ecuaciones no lineales, con interfaz gráfica para visualización, comparación de resultados y generación de reportes de convergencia.

---

## 📈 Criterios de Evaluación

- Exposición (30%)
- Problemario (40%)
- Proyecto (30%)

---

[⬅️ Volver al README principal](../README.md)
