# Tema 4: Diferenciación e Integración Numérica

## 🌍 Contexto Fundamental

En las ciencias aplicadas y la ingeniería, muchas veces se trabaja con funciones cuya derivada o integral no puede obtenerse de manera exacta. Ya sea por la complejidad de la función o porque los datos provienen de experimentos, surge la necesidad de utilizar **métodos numéricos** para estimar derivadas e integrales.

Por ejemplo:

- Analizar la velocidad instantánea de un vehículo 🚗 a partir de datos experimentales de posición.
- Calcular el área bajo la curva de una función de comportamiento no conocido con precisión 📈.
- Estimar flujos de calor o cargas eléctricas en sistemas dinámicos ⚡ donde las expresiones analíticas no son viables.

Aquí es donde entran en juego los métodos de **diferenciación e integración numérica**, permitiendo obtener aproximaciones útiles con alta precisión y eficiencia computacional.

---

## 📌 Importancia de la Diferenciación e Integración Numérica

> "Son técnicas que permiten traducir funciones continuas en cálculos discretos para resolver problemas reales."

**Aplicaciones principales:**
- Estimación de derivadas cuando no es posible derivar analíticamente.
- Cálculo de áreas, volúmenes y acumulados en procesos físicos.
- Solución de ecuaciones diferenciales mediante métodos numéricos.
- Modelado en ingeniería, física, biología y economía.

---

## 🎓 Actividades de Aprendizaje

### 🧠 T4-E1: Mapa Conceptual

**Indicaciones del docente**  
Elaborar un mapa conceptual que integre los principales métodos numéricos de diferenciación e integración, mostrando sus fórmulas, características, ventajas y casos de uso.

**Métodos incluidos:**
- Fórmulas de tres y cinco puntos para derivación.
- Método del trapecio.
- Regla de Simpson (1/3 y 3/8).
- Cuadratura Gaussiana.

[🔗 Ver mapa mental (miro)](https://miro.com/welcomeonboard/ZGpDVzBCY1RJWjRIUjFUUFJFMm9qZ3RESmFCN1FCdjlqTmNCaTRHT1NaL0d3MVA4SmpsT0lhL3RQUVpzODZ0MEE0NENNdUY3Y2ZUK3FXbFFOZU11QWxUUXZ3Q1FoMGxpTjduM3JiRXRNdHpPZDJxY3Iwdjd2c1pmSTE5RnhtcmFzVXVvMm53MW9OWFg5bkJoVXZxdFhRPT0hdjE=?share_link_id=110120835579&authuser=0) 
[🔗 Ver presentación (Canva)](https://www.canva.com/design/DAGjK984lkk/DpiriI4EPM5mfVAWeRNfKg/view?utm_content=DAGjK984lkk&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he46a7ff251) 

---

### 💻 T4-E2: Aplicación Práctica y Código

**Descripción:**  
Desarrollar programas en Python para implementar y comparar diferentes métodos de diferenciación e integración numérica. Cada ejercicio incluye el planteamiento del problema, el código implementado y la interpretación de resultados.

---

#### 📐 Método del Trapecio

**Descripción del método:**  
Este método aproxima el área bajo la curva dividiendo el intervalo en segmentos donde cada subárea es considerada un trapecio. Puede ser simple o compuesto para mayor precisión.

**Ejercicio resuelto:**  
Estimar el valor de la integral definida de \( f(x) = \ln(x) \) en el intervalo \([1, 2]\).

[🔗 Ver código del método de Gauss (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema4/Metodo%20del%20trapecio.py)

---

#### 📐 Regla de Simpson 1/3

**Descripción del método:**  
Este método utiliza parábolas para aproximar el área bajo la curva. Es muy preciso para funciones suaves y se aplica en intervalos pares.

**Ejercicio resuelto:**  
Calcular la integral de \( f(x) = e^{-x^2} \) en \([0, 1]\).

[🔗 Ver código de Simpson 1/3 (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema4/integracion/simpson_1_3.py)

---

#### 📐 Regla de Simpson 3/8

**Descripción del método:**  
Simpson 3/8 es una variante que utiliza polinomios cúbicos. Es útil cuando el número de subintervalos es múltiplo de 3.

**Ejercicio resuelto:**  
Aproximar la integral de \( f(x) = \sqrt{1 + x^4} \) en \([0, 3]\).

[🔗 Ver código de Simpson 3/8 (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema4/integracion/simpson_3_8.py)

---

#### 📐 Cuadratura Gaussiana

**Descripción del método:**  
Este método transforma la integral definida a una forma estándar y utiliza puntos y pesos especiales (raíces de polinomios de Legendre) para calcular una aproximación muy precisa.

**Ejercicio resuelto:**  
Evaluar la integral de \( f(x) = \frac{1}{1 + x^2} \) en \([-1, 1]\) usando 2 y 3 puntos.

[🔗 Ver código de Cuadratura Gaussiana (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema4/integracion/cuadratura_gaussiana.py)

---

Cada implementación incluye gráficos comparativos, análisis de errores y recomendaciones de uso según la función o intervalo.

[🔗 Ver carpeta completa de integración numérica](https://github.com/IvanPedroSuarez/Metodos-Numericos-/tree/master/codigos/tema4/integracion)


### 🚀 T4-E3: Proyecto Final

**Descripción:**  
Aplicación de los métodos estudiados a un caso real o simulado. El proyecto incluyó:

- Desarrollo del código en Python.
- Interpretación de resultados.
- Visualización gráfica de la función, derivadas e integrales.
- Comparación de precisión entre métodos.

[🔗 Ver notebook del proyecto (Jupyter Notebook)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/tree/master/codigos/tema4/proyecto_final)

---

[⬅️ Volver al README principal](../README.md)

