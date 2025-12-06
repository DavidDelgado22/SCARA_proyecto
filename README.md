# Robot SCARA RRP – Cinemática directa y control con Arduino

Repositorio del proyecto de **cinemática directa y control de un robot SCARA RRP** usando:
- Python (Jupyter Notebook) para el cálculo de la cinemática directa.
- Arduino para el control de tres servomotores.
- Un **GIF de evidencia** que muestra la ejecución del Notebook y el movimiento del robot físico.

---

## 1. Descripción del proyecto

El proyecto implementa la **cinemática directa** de un robot SCARA RRP de 3 grados de libertad:

- Dos articulaciones **revolutas** (q1 y q2) en el plano XY.
- Una articulación **prismática** (d3) que controla el eje Z (subida y bajada del efector).

El flujo general es:

1. El usuario introduce valores articulares *(q1, q2 en grados; d3 en milímetros)*.
2. El Notebook convierte las variables a radianes/metros y calcula la posición del efector \((x, y, z)\) usando el modelo DH.
3. Se muestran las matrices \(A_1, A_2, A_3\) y la matriz homogénea completa \(T\).
4. Se envían los valores articulares al Arduino a través del puerto serial.
5. El Arduino mapea estos valores a ángulos de servomotor y mueve el robot físico.
6. Se generan pruebas experimentales y un **GIF de evidencia** que muestra:
   - La ejecución del Notebook.
   - El movimiento del robot en el mundo real.

---

## 2. Estructura del repositorio

```text
.
├─ scara_direct_kinematics.ipynb   # Notebook principal
├─ arduino_scara.ino               # Código de Arduino
├─ media/
│   └─ scara_fk_demo.gif           # GIF de evidencia
└─ README.md                       # Este documento
