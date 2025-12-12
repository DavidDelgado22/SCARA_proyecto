# Robot SCARA RRP – Cinemática directa e inversa y control con Arduino

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
├─ GIF
└─ README.md                       # Este documento
```

# Requerimientos

- Python (probado con 3.10 – 3.12)

Instalar:

pip install numpy pyserial matplotlib imageio

- Arduino

Servo.h (incluida por defecto)

Puerto serial configurado a 115200 baud

# ▶️ Ejecución
1️⃣ Ejecutar el Notebook

Abrir Jupyter Notebook:

jupyter notebook


Cargar scara_direct_kinematics.ipynb

Conectar Arduino al puerto COM correspondiente

Ejecutar:

Selección del puerto serial

Ingreso de q1, q2, d3

Cálculo FK

Envío a Arduino

Generación del GIF (automático)

2️⃣ Cargar el Arduino

Sube el archivo:

arduino_scara.ino


Este recibe:

q1_rad, q2_rad, d3_m, gripper


y mueve los servos en tiempo real.

# Evidencia

El GIF se encuentra en:

/media/scara_evidencia.gif


Incluye:

Ejecución del Notebook

Cálculo de (x, y, z)

Movimiento del robot físico

# Autores

- Kevyn David Delgado Gómez, Eduardo Montiel Salazar
- Ingeniería Mecatrónica – Cinemática Directa SCARA RRP




