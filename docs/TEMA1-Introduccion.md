# Tema 1: Introducción a los Métodos Numéricos

## 🌍 Contexto Fundamental
En un mundo donde los problemas científicos e ingenieriles son cada vez más complejos, **los métodos numéricos emergen como el puente entre la teoría matemática y las soluciones prácticas**. Imagina intentar:

- Predecir el clima ☁️
- Optimizar el diseño de un avión ✈️
- Entrenar modelos de inteligencia artificial 🤖

Todos estos desafíos comparten una realidad: **no pueden resolverse solo con lápiz y papel**. En este primer tema exploraremos los fundamentos que hacen posible estas soluciones computacionales.

---

## 📌 Importancia de los Métodos Numéricos
> "Son el lenguaje secreto que traduce problemas del mundo real a algoritmos computables"

**Aplicaciones clave:**
- ✅ Solución de ecuaciones no resolubles analíticamente (ej: ecuaciones diferenciales no lineales)
- ✅ Optimización de procesos en ingeniería y ciencia de datos
- ✅ Simulación de sistemas complejos (desde modelos climáticos hasta dinámica de fluidos)

![Proceso numérico](https://via.placeholder.com/600x200?text=Diagrama+Flujo+Métodos+Numéricos) <!-- Reemplazar con imagen real -->

---

## 🔍 Conceptos Básicos

### 1. Cifras Significativas

# Ejemplo práctico
pi_aproximado = 3.14    # 3 cifras significativas
pi_preciso = 3.141592    # 7 cifras significativas

---

##  Precicion vs Exavtitud 

| Concepto   | Definición                              | Ejemplo Visual                  | Representación Matemática       |
|------------|----------------------------------------|---------------------------------|----------------------------------|
| **Precisión** | Consistencia en resultados repetidos   | 🎯 → • • • (agrupados pero desviados) | `Desviación estándar pequeña`    |
| **Exactitud** | Proximidad al valor verdadero          | 🎯 → · · · (dispersos pero cerca del centro) | `Error absoluto pequeño`         |


##  Tipos de errores mas comunes en metodos numericos:

| Tipo de Error         | Causa                                                                 | Ejemplo                                                                 | Fórmula/Cálculo                      |
|-----------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------|
| **Truncamiento**      | Aproximar un proceso infinito con uno finito                          | Usar solo 3 términos de una serie de Taylor para `sin(x)`               | `Error = Valor real - Valor truncado`|
| **Redondeo**          | Limitación en dígitos almacenados por la computadora                  | `1/3 ≈ 0.333333` (en lugar de 0.333...)                                | `float(x)` en Python                 |
| **Absoluto**          | Diferencia entre valor real y aproximado                              | π ≈ 3.1416 vs 3.14 → Error = 0.0016                                    | `\|Valor real - Aproximación\|`      |
| **Relativo**          | Error en porcentaje respecto al valor real                            | Si error absoluto = 0.1 y valor real = 10 → Error relativo = 1%        | `(Error absoluto / Valor real) × 100%` |


## 🎓 Actividades de Aprendizaje

### 📊 T1-E1: Mapa Conceptual de Errores
**Objetivo:** Visualizar las relaciones entre los tipos de errores numéricos mediante un diagrama interactivo.

🔹 *Características principales:*
- Análisis comparativo entre errores de truncamiento y redondeo
- Ejemplos gráficos de propagación de errores
- Desarrollo colaborativo en equipo

[[Ver Mapa Conceptual en Canva](https://www.canva.com/design/DAGd4cTWnj8/TWtBOVQzBepaHcPNFX8W0Q/edit?utm_content=DAGd4cTWnj8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

### 💻 T1-E2: Problemario de Errores Numéricos
**CActididad enfocada en la demostracion de los diferentes tipos de errores en metodos numericos as como una explicacion de estos.**
[📦 ver codgios usados para la actividad T1 ----E2----Problemario ](/codigos/tema1-introduccion/)


### 
**Evaluacion**
- Finalmente se realizo una evaluacion en linea para reforzar todos los conocimientos adquiridos.


