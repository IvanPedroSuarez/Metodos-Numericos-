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

### 🧠 T3-E1: Mapa Mental de Métodos Numéricos

**Indicaciones del docente**  
Realizar un mapa mental que resuma y compare los principales métodos para resolver sistemas de ecuaciones lineales:

- Eliminación Gaussiana  
- Gauss-Jordan  
- Método de Jacobi  
- Método de Gauss-Seidel

**Contenido del mapa mental:**
- Concepto de cada método
- Requisitos para su aplicación (por ejemplo: diagonal dominante, matriz cuadrada, etc.)
- Ventajas y desventajas
- Tipos de sistemas que pueden resolver
- Comparativa visual de los métodos iterativos vs directos

[🔗 Ver presentación sobre el Mapa Mental (Lucida)](https://lucid.app/lucidspark/06170dd7-87af-417c-a10a-c7c702da8f67/edit?viewport_loc=-20381%2C16382%2C21347%2C10146%2C0_0&invitationId=inv_fae549c6-18d6-451b-b564-cb42654dd187)

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

[🔗 Ver código del método de Gauss (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Eliminacion%20Gaussiana%20con%20pivote.py)

---

#### 2. Método de Gauss-Jordan

**Descripción:**  
Extiende el método de Gauss, eliminando también los elementos por encima de la diagonal principal para obtener una matriz identidad.

**Ejercicio resuelto:**  
Resolver el mismo sistema de 3x3 por Gauss-Jordan.

[🔗 Ver código del método de Gauss-Jordan (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20Gauss%20Jordan.py)

---

#### 3. Método de Jacobi

**Descripción:**  
Es un método iterativo que calcula nuevas aproximaciones de cada variable usando los valores de la iteración anterior. Requiere matrices diagonales dominantes.

**Ejercicio resuelto:**  
Resolver un sistema iterativamente con Jacobi.

[🔗 Ver código del método de Jacobi (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20de%20Jacobi.py)

---

#### 4. Método de Gauss-Seidel

**Descripción:**  
Similar al de Jacobi, pero utiliza inmediatamente los nuevos valores calculados en cada iteración, lo cual acelera la convergencia en muchos casos.

**Ejercicio resuelto:**  
Aplicar Gauss-Seidel a un sistema de 3x3.

[🔗 Ver código del método de Gauss-Seidel (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/Metodo%20de%20Gauss-Seidel.py)

---

Cada ejercicio incluye el análisis del procedimiento, la interpretación de resultados y la discusión de posibles dificultades o casos especiales.  
[🔗 Ver todos los códigos de implementación](https://github.com/IvanPedroSuarez/Metodos-Numericos-/tree/master/codigos/tema3)

---

## Caso de prueba: Ejemplo: Cuando el pivote de una columna es 0 Gauss-Jordan 
Resolver el siguiente sistema de ecuaciones lineales utilizando el método de eliminación Gauss-Jordan con pivoteo parcial. El usuario ingresa la matriz aumentada correspondiente y el programa muestra paso a paso el proceso hasta encontrar la solución:
                                                            
                                                            
**x−2y=1**
**2x−4y=3**
​

[🔗 Ver caso de prueba ](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema3/CasoPrueba.py)

¿Por qué falla?El método falla cuando, durante el proceso, el pivote de una columna es cero y no hay ninguna fila disponible para intercambiar que tenga un valor distinto de cero en esa columna. Esto significa que el sistema no tiene solución única: puede ser inconsistente (como en este ejemplo, donde las ecuaciones son proporcionales pero los términos independientes no coinciden) o tener infinitas soluciones.
En este caso, la segunda fila se transforma en [0, 0, 1], lo que representa una ecuación imposible (0 = 1), por lo que el algoritmo detecta la inconsistencia y lanza un error para evitar cálculos inválidos.


---

### 🚀 T3 -- E3 --- Proyecto

**Descripción:**  
El proyecto final consiste en resolver un sistema de ecuaciones lineales utilizando **Excel**, aplicando paso a paso el método de **Gauss-Jordan** con fórmulas y referencias.  

[🔗 Ver documento de la evaluación](https://docs.google.com/document/d/1KVxzQzMgrfOevVSGcP5M272uYC6VKLRiAVBtBGRaipY/edit?usp=sharing)

---

[⬅️ Volver al README principal](../README.md)

