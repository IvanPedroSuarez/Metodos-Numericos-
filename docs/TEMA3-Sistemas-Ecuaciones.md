# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

## 🌍 Contexto Fundamental

En las ciencias e ingeniería, es común enfrentarse a problemas que requieren la resolución de múltiples ecuaciones simultáneamente. Estos sistemas de ecuaciones lineales aparecen en contextos como:

- El análisis estructural de puentes y edificios 🏗️, donde se equilibran fuerzas en múltiples direcciones.
- La simulación de redes eléctricas ⚡, en las que se calculan corrientes y voltajes en mallas complejas.
- La modelación económica 📉, en la que múltiples variables interdependientes deben satisfacer restricciones simultáneas.

Dado que resolver estos sistemas de forma manual no es práctico cuando el número de ecuaciones crece, se emplean **métodos numéricos** que permiten obtener soluciones aproximadas de manera eficiente mediante el uso de computadoras. Estos métodos, como **Gauss, Gauss-Jordan, LU, Jacobi y Gauss-Seidel**, son fundamentales en simulación, análisis de datos y cálculo científico.

---

## 📌 Importancia de los Métodos de Solución

> "Son las claves para desentrañar sistemas complejos que gobiernan el comportamiento del mundo físico y social."

**Aplicaciones principales:**
- Resolver sistemas lineales grandes y/o mal condicionados.
- Análisis estructural y térmico.
- Optimización y modelos predictivos.
- Simulaciones de fenómenos físicos, químicos y económicos.

---

## 🎓 Actividades de Aprendizaje

### 📊 T3-E1: Exposición de Métodos Numéricos

**Indicaciones del docente**  
Formarse en equipos e investigar los diferentes métodos de solución para sistemas de ecuaciones lineales (Gauss, Gauss-Jordan, matrices inversas, factorización LU, Jacobi, Gauss-Seidel, etc). Elaborar un informe o presentación.

El método asignado fue **Gauss-Seidel**, y se abordaron los siguientes puntos:

- Introducción del método  
- ¿Qué es?  
- Fórmula  
- Pasos para aplicar el método  
- Requisitos para aplicar el método  
- Ejemplo (video)  
- Aplicaciones  
- Ventajas y Desventajas  
- Convergencia y errores  
- Tabla comparativa  
- Desafío  
- Conclusión general

[🔗 Ver presentación sobre el método de Gauss-Seidel (Canva)](https://www.canva.com/)

---

### 💻 T3-E2: Problemario de Métodos de Solución

**Descripción:**  
Ejercicios prácticos enfocados en la aplicación de métodos numéricos para resolver sistemas de ecuaciones lineales. Cada subapartado describe brevemente el método y presenta un ejercicio resuelto con Python.

---

#### 1. Método de Eliminacion Gaussiana

**Descripción:**  
El método de eliminación de Gauss transforma el sistema original en uno triangular superior mediante operaciones fila, para luego resolver por sustitución hacia atrás.

**Ejercicio resuelto:**  
Resolver un sistema de 3x3 ecuaciones con coeficientes conocidos.

[🔗 Ver código del método de Gauss (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Eliminacio20%nGaussiana20%con20%pivote.py)

---

#### 2. Método de Gauss-Jordan

**Descripción:**  
Extiende el método de Gauss, eliminando también los elementos por encima de la diagonal principal para obtener una matriz identidad.

**Ejercicio resuelto:**  
Resolver el mismo sistema de 3x3 por Gauss-Jordan.

[🔗 Ver código del método de Gauss-Jordan (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20de%20Gauss-Jordan.py)

---

#### 3. Método de la Matriz Inversa

**Descripción:**  
Si una matriz A es invertible, el sistema \( Ax = b \) se puede resolver mediante \( x = A^{-1}b \).

**Ejercicio resuelto:**  
Usar la matriz inversa para resolver un sistema lineal.

[🔗 Ver código del método de la Matriz Inversa (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20de%20matriz%20inversa.py)

---

#### 4. Método de Factorización LU

**Descripción:**  
Descompone la matriz A en el producto de una matriz triangular inferior (L) y una superior (U), simplificando la resolución de múltiples sistemas con la misma matriz A.

**Ejercicio resuelto:**  
Aplicar la factorización LU para resolver un sistema.

[🔗 Ver código del método LU (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20LU.py)

---

#### 5. Método de Jacobi

**Descripción:**  
Es un método iterativo que calcula nuevas aproximaciones de cada variable usando los valores de la iteración anterior. Requiere matrices diagonales dominantes.

**Ejercicio resuelto:**  
Resolver un sistema iterativamente con Jacobi.

[🔗 Ver código del método de Jacobi (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20Jacobi.py)

---

#### 6. Método de Gauss-Seidel

**Descripción:**  
Similar al de Jacobi, pero utiliza inmediatamente los nuevos valores calculados en cada iteración, lo cual acelera la convergencia en muchos casos.

**Ejercicio resuelto:**  
Aplicar Gauss-Seidel a un sistema de 3x3.

[🔗 Ver código del método de Gauss-Seidel (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20Gauss-Seidel.py)

---

Cada ejercicio incluye el análisis del procedimiento, la interpretación de resultados y la discusión de posibles dificultades o casos especiales.  
[🔗 Ver todos los códigos de implementación](https://github.com/IvanPedroSuarez/Metodos-Numericos-/tree/master/codigos/tema3)

---

### 🚀 T3 -- E3 --- Proyecto

**Descripción:**  
El proyecto final consiste en resolver un sistema de ecuaciones lineales utilizando **Excel**, aplicando paso a paso el método de **Gauss-Jordan** con fórmulas y referencias.  

[🔗 Ver documento de la evaluación en formato .xlsx](https://docs.google.com/spreadsheets/)

---

[⬅️ Volver al README principal](../README.md)

