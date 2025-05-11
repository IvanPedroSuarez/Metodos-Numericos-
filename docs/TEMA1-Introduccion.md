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

---

## 🔍 Conceptos Básicos

### 1. Cifras Significativas

Ejemplo práctico
pi_aproximado = 3.14 # 3 cifras significativas
pi_preciso = 3.141592 # 7 cifras significativas


---

## Precicion vs Exavtitud

| Concepto   | Definición                              | Ejemplo Visual                  | Representación Matemática       |
|------------|----------------------------------------|---------------------------------|----------------------------------|
| **Precisión** | Consistencia en resultados repetidos   | 🎯 → • • • (agrupados pero desviados) | `Desviación estándar pequeña`    |
| **Exactitud** | Proximidad al valor verdadero          | 🎯 → · · · (dispersos pero cerca del centro) | `Error absoluto pequeño`         |

## Tipos de errores mas comunes en metodos numericos:

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

> **Actividad enfocada en la demostración de los diferentes tipos de errores en métodos numéricos así como una explicación de estos.**

### 1️⃣ Errores de Precisión

**Código de ejemplo:**
python
Copy Code
# Ejemplo de error de precisión con suma repetida
suma = 0
for i in range(10000):
    suma += 0.0001

print(f"Valor esperado: 1.0")
print(f"Valor obtenido: {suma}")
print(f"Error absoluto: {abs(suma - 1.0)}")
print(f"Error relativo: {abs(suma - 1.0) / 1.0}")
🔍 Observación: Este ejemplo muestra cómo la acumulación de pequeños errores en operaciones repetidas puede llevar a resultados ligeramente diferentes de los esperados.

2️⃣ Errores de Redondeo
Código de ejemplo:

python
Copy Code
# Ejemplo de error de redondeo con números decimales
x = 0.1 + 0.1 + 0.1
print(f"Valor esperado: 0.3")
print(f"Valor obtenido: {x}")
print(f"Error absoluto: {abs(x - 0.3)}")
print(f"Error relativo: {abs(x - 0.3) / 0.3}")
💡 Nota: Este error ocurre debido a que 0.1 no puede representarse exactamente en binario, llevando a pequeñas discrepancias en los cálculos.

3️⃣ Errores de Truncamiento
Código de ejemplo:

python
Copy Code
import math

# Ejemplo de error de truncamiento: Aproximación de e usando series de Taylor
def aproximar_e(n):
    e_aprox = 0
    for i in range(n):
        e_aprox += 1 / math.factorial(i)
    return e_aprox

n_terminos = 5
e_aproximado = aproximar_e(n_terminos)
e_real = math.e

print(f"Valor esperado (e): {e_real}")
print(f"Valor aproximado: {e_aproximado}")
print(f"Error absoluto: {abs(e_real - e_aproximado)}")
print(f"Error relativo: {abs(e_real - e_aproximado) / e_real}")
📝 Explicación: Este ejemplo muestra cómo el error de truncamiento ocurre al aproximar una serie infinita con un número finito de términos.

### Evaluación
- Finalmente se realizo una evaluacion en linea para reforzar todos los conocimientos adquiridos.
