# Tema 6: Solución de ecuaciones diferenciales

## 🧩 Contexto Fundamental

En la ciencia, la ingeniería y la tecnología, muchos fenómenos reales se describen mediante ecuaciones diferenciales. Estas ecuaciones permiten modelar cómo cambian las variables en el tiempo o el espacio, y son esenciales para entender procesos dinámicos en sistemas físicos, biológicos, económicos y más. Sin embargo, la mayoría de las ecuaciones diferenciales no pueden resolverse de forma exacta, por lo que es necesario recurrir a métodos numéricos para obtener soluciones aproximadas. Por ejemplo:

- Predecir la evolución de la temperatura en un objeto que se enfría o calienta con el tiempo 🌡️.
- Simular la trayectoria de un proyectil o satélite bajo la influencia de la gravedad 🚀.
- Modelar el crecimiento de una población bacteriana limitada por recursos 🦠.
- Analizar la concentración de un medicamento en la sangre tras una dosis 💊.
- Estudiar la respuesta de un circuito eléctrico ante una señal variable ⚡.

En estos escenarios, los **métodos numéricos para ecuaciones diferenciales** se convierten en herramientas fundamentales. Permiten aproximar la solución de problemas donde no existe una fórmula explícita, facilitando la simulación, el diseño y el análisis de sistemas complejos en la vida real.
---


## 🎓 Actividades de Aprendizaje

## 📊 T6   -E1-   Exposición 

**Indicaciones del docente**  
     1.- Se conformarán en equipo ( elección libre y no más de 5 integrantes )
      2.- En trabajo grupal investigarán las Solución de ecuaciones diferenciales( 
                    6.1 Métodos de un paso.
                   6.2 Método de pasos múltiples.
                   6.3 Sistemas de ecuaciones diferenciales ordinarias.), uno por equipo (ver imagen adjunta)



link para ver la presentacion (https://www.canva.com/design/DAGn5cuHz-w/0U6xB8mzlZnP43LQbO_TZA/edit?utm_content=DAGn5cuHz-w&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton.)

---
## 1. Método de Euler
**Descripción del método:**
El método de Euler es una técnica numérica simple y directa para aproximar soluciones de ecuaciones diferenciales ordinarias de primer orden. Consiste en avanzar paso a paso usando la pendiente local, lo que lo hace fácil de implementar pero con precisión limitada para pasos grandes.

**Ejercicio resuelto:**  
En el diseño de sensores IoT y sistemas electrónicos, es fundamental conocer el comportamiento de los circuitos RC, especialmente durante la carga y descarga de un capacitor. Supón que se conecta un capacitor de 100 μF en serie con una resistencia de 1 kΩ a una fuente de 5V. Se desea estimar cómo varía la tensión en el capacitor durante los primeros 0.2 segundos después de aplicar el voltaje. Este análisis es crucial para determinar la velocidad de respuesta del circuito, optimizar el filtrado de señales y garantizar que el sistema funcione correctamente en aplicaciones de adquisición de datos o transmisión inalámbrica.

[🔗 Ver código del método de Euler (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/euler.py)

---

## 2. Adams-Bashforth-Moulton (Predictor-Corrector de 4 pasos)

**Descripción del método:**
El método Adams-Bashforth-Moulton es un esquema predictor-corrector de pasos múltiples que combina un paso explícito (Adams-Bashforth) y uno implícito (Adams-Moulton) para lograr mayor precisión y estabilidad en la solución de ecuaciones diferenciales ordinarias.


**Ejercicio resuelto:**  
En la industria automotriz, el diseño de sistemas de suspensión es esencial para garantizar la seguridad y el confort de los pasajeros. Un amortiguador puede modelarse como un sistema masa-resorte-amortiguador, donde la masa representa la carrocería del vehículo, el resorte simula la elasticidad de la suspensión y el amortiguador disipa la energía de las vibraciones. Supón que, tras pasar por un bache, la suspensión se desplaza 5 cm y parte del reposo. Se busca simular el desplazamiento y la velocidad de la suspensión durante los primeros 3 segundos, usando parámetros realistas (m = 60 kg, c = 300 N·s/m, k = 20,000 N/m). Este análisis permite evaluar si el sistema disipa la energía de manera eficiente y si la carrocería retorna rápidamente a su posición de equilibrio, lo cual es clave para el diseño de vehículos todo terreno y urbanos.

[🔗 Ver código de Adams-Bashforth-Moulton (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/abm.py)

---

## 3. Método de Taylor de segundo orden

**Descripción del método:**
El método de Taylor de segundo orden utiliza la expansión en serie de Taylor hasta el término cuadrático para aproximar la solución de una ecuación diferencial. Esto permite mejorar la precisión respecto a métodos de primer orden como Euler, considerando la curvatura de la solución.

**Ejercicio resuelto:**  
En la vida cotidiana y en la industria alimentaria, es importante predecir cómo se enfría una bebida caliente en un ambiente más frío. Por ejemplo, una taza de café recién hecho a 90°C se deja en una habitación a 22°C. La velocidad de enfriamiento depende de la diferencia de temperatura y sigue la ley de enfriamiento de Newton. Se desea estimar la temperatura del café durante los primeros 10 minutos, usando un coeficiente de enfriamiento típico de k = 0.15 min⁻¹. Este tipo de análisis es útil para optimizar procesos de servicio en cafeterías, garantizar la seguridad alimentaria y mejorar la experiencia del consumidor.

[🔗 Ver código del método de Taylor (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/taylor.py)

---

## 4. Método de Euler para sistemas

**Descripción del método:**
El método de Euler para sistemas extiende la idea del método de Euler a sistemas de ecuaciones diferenciales, permitiendo simular la evolución conjunta de varias variables dependientes.

**Ejercicio resuelto:**  
El estudio de trayectorias de proyectiles es fundamental en física, deportes y balística. Imagina que se lanza una pelota desde el suelo con una velocidad inicial de 12 m/s en el eje horizontal y 18 m/s en el eje vertical. Se busca simular la trayectoria completa de la pelota hasta que toque el suelo, considerando únicamente la gravedad y despreciando la resistencia del aire. Este tipo de simulación es útil para entrenadores deportivos, ingenieros y desarrolladores de videojuegos que buscan modelar trayectorias realistas y optimizar estrategias de lanzamiento.

[🔗 Ver código de Euler para sistemas (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/eulerps.py)

---

## 5. Runge–Kutta RK4 (una EDO)

**Descripción del método:**
El método de Runge-Kutta de cuarto orden (RK4) es uno de los métodos más populares y precisos para resolver ecuaciones diferenciales ordinarias. Utiliza cuatro evaluaciones de la función en cada paso para lograr alta precisión sin requerir derivadas adicionales.

**Ejercicio resuelto:**  
En microbiología y biotecnología, es esencial predecir el crecimiento de colonias bacterianas en un medio con recursos limitados. Supón que una colonia parte de 100,000 bacterias y crece con una tasa de 1.2 h⁻¹, pero el crecimiento se ralentiza a medida que se acerca a la capacidad máxima del medio (10 millones de bacterias). Se simula el crecimiento durante 8 horas usando el método RK4. Este análisis ayuda a planificar experimentos, optimizar la producción de biomasa y prevenir la sobrepoblación en biorreactores.

[🔗 Ver código de Runge-Kutta RK4 (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/rk4.py)

---

## 6. Runge–Kutta RK4 para sistemas

**Descripción del método:**
El método RK4 para sistemas permite resolver simultáneamente varias ecuaciones diferenciales acopladas, aplicando el esquema de Runge-Kutta de cuarto orden a cada variable del sistema.

**Ejercicio resuelto:**  
En ecología, el modelo Lotka-Volterra describe la interacción entre una población de presas y sus depredadores. Supón que en un ecosistema hay 25 presas y 5 depredadores al inicio, con tasas de crecimiento y depredación conocidas. Se simula la evolución de ambas poblaciones durante 30 días. Este tipo de simulación es fundamental para biólogos y gestores ambientales, ya que permite prever ciclos poblacionales, evaluar el impacto de la caza o la introducción de especies, y diseñar estrategias de conservación.

[🔗 Ver código de Runge-Kutta RK4 para sistemas (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/rk4s.py)

---

## 7. Adams-Bashforth de 2 pasos

**Descripción del método:**
El método de Adams-Bashforth de 2 pasos es un método explícito de pasos múltiples que utiliza la información de los dos pasos anteriores para predecir el siguiente valor de la solución, mejorando la precisión respecto a métodos de un solo paso.

**Ejercicio resuelto:**  
En ingeniería ambiental, es común analizar la disminución de la concentración de contaminantes en cuerpos de agua o aire. Supón que un derrame químico eleva la concentración de un contaminante a 120 ppm en un lago, y que la degradación sigue una ley de decaimiento exponencial con una constante de 0.3 día⁻¹. Se desea estimar la concentración durante el primer día, usando el método de Adams-Bashforth de 2 pasos. Este análisis ayuda a planificar acciones de remediación y a evaluar el tiempo necesario para que el ecosistema recupere condiciones seguras.

[🔗 Ver código de Adams-Bashforth 2 pasos (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/ab2.py)

---

## 8. Linealización (Newton–Raphson multivariable)

**Descripción del método:**
El método de Newton-Raphson multivariable es una técnica iterativa para encontrar soluciones aproximadas a sistemas de ecuaciones no lineales, utilizando el Jacobiano para actualizar las estimaciones en cada iteración.

**Ejercicio resuelto:**  
En robótica industrial, la cinemática inversa es esencial para controlar brazos robóticos y posicionar herramientas con precisión. Supón que un robot de dos eslabones, cada uno de 1 metro, debe alcanzar el punto (1.5, 0.8) en el plano. Se busca calcular los ángulos de las articulaciones que permiten alcanzar esa posición, resolviendo el sistema no lineal mediante el método de Newton-Raphson. Este procedimiento es clave en la programación de robots para manufactura, ensamblaje y cirugía asistida por computadora.

[🔗 Ver código de Newton-Raphson multivariable (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/linea.py)

---

## 9. Adams-Moulton 4 pasos

**Ejercicio resuelto:**  
En medicina y farmacología, es fundamental conocer cómo varía la concentración de un medicamento en sangre tras una inyección intravenosa. Supón que se administra una dosis de 8 mg/L de un fármaco que se elimina con una constante de 0.6 h⁻¹. Se desea estimar la concentración durante las primeras 12 horas usando el método de Adams-Moulton de 4 pasos. Este análisis es crucial para diseñar esquemas de dosificación seguros y efectivos, evitando tanto la toxicidad como la ineficacia terapéutica.

[🔗 Ver código de Adams-Moulton 4 pasos (Python)](https://github.com/IvanPedroSuarez/Metodos-Numericos-/blob/master/codigos/tema6/am4.py)

---

### 🚀 T5 - E3  -  Programa 

**Descripción del método:**
El método de Adams-Moulton de 4 pasos es un método implícito de pasos múltiples que utiliza información de los cuatro pasos anteriores para corregir la predicción de la solución, logrando alta precisión y estabilidad en problemas de decaimiento o crecimiento lento.

**Descripción:**  
Para la evaluación del tema el docente planteo un problema que debia ser resuelto a travez del metodo de iterpolacion polinomica, no sin antes poder
explicar (con nuestras propias palabras) el algoritmo del metodo. Posterioirmente el planteamiento, pseudocodigo, codigo y resolucion del problema fueron plasmados en un documento.
[🔗 Ver documento de la evaluacion en formato .docs, ](https://docs.google.com/document/d/1dbSx0OTLwGttwcV7lvidtpZdW-mco7OTFTi_u1A4z-U/edit?usp=sharing)





[⬅️ Volver al README principal](../README.md)
