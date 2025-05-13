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
Ejercicios prácticos enfocados en la aplicación de los métodos numéricos para encontrar raíces de ecuaciones no lineales. Cada subapartado corresponde a un método diferente, con ejemplos representativos.

#### 1. Método de Bisección

**Ejemplo:**  
Aproxima la raíz de \( f(x) = x^3 - 25 \) en el intervalo \([1, 3]\).

**Procedimiento:**  
Se seleccionan los extremos del intervalo, se verifica el cambio de signo, se calcula el punto medio y se repite el proceso hasta alcanzar la precisión deseada.

**Resultado:**  
Después de varias iteraciones, se obtiene una raíz aproximada en \( x \approx 2.924 \).

[🔗 Ver código de metodo de biseccion (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema2/Método%20de%20biseccion.py)


---

#### 2. Método de la Regla Falsa

**Ejemplo:**  
Encuentra la raíz de \( f(x) = x^3 - x - 1 \) en el intervalo \([1, 2]\).

**Procedimiento:**  
Se usan los extremos del intervalo y la fórmula de la regla falsa para aproximar la raíz, actualizando el intervalo en cada iteración.

**Resultado:**  
El método converge a una raíz aproximada dentro del intervalo.

---

#### 3. Método de Punto Fijo

**Ejemplo:**  
Resuelve \( f(x) = e^{-x} - x \) usando una función de iteración adecuada, por ejemplo \( x = e^{-x} \).

**Procedimiento:**  
Se elige un valor inicial y se itera usando la función de punto fijo hasta que el error absoluto sea suficientemente pequeño.

**Resultado:**  
La raíz se aproxima a \( x \approx 0.5671 \).

---

#### 4. Método de Newton-Raphson

**Ejemplo:**  
Determina la raíz de \( f(x) = x^3 - x - 1 \) usando un valor inicial \( x_0 = 1.5 \).

**Procedimiento:**  
Se calcula la derivada, se aplica la fórmula de Newton-Raphson y se repite hasta alcanzar la tolerancia deseada.

**Resultado:**  
El método converge rápidamente a la raíz real de la función.

---

#### 5. Método de la Secante

**Ejemplo:**  
Encuentra la raíz de \( f(x) = \cos(x) - x \) usando valores iniciales \( x_0 = 0.5 \) y \( x_1 = 1 \).

**Procedimiento:**  
Se aplica la fórmula de la secante iterativamente hasta que el error relativo sea suficientemente pequeño.

**Resultado:**  
La raíz se aproxima a \( x \approx 0.739 \).

---

Cada ejercicio incluye el análisis del procedimiento, la interpretación de resultados y la discusión de posibles dificultades o casos especiales.  
[🔗 Ver códigos de implementación](https://github.com/tu-usuario/tu-repo/tree/master/tema2)

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
