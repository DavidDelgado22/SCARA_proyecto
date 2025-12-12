# Robot SCARA RRP – Cinemática directa e inversa y control con Arduino

Repositorio del proyecto de **cinemática directa e inversa y control de un robot SCARA RRP** desarrollado como parte de la asignatura de Robótica, integrando modelado matemático, simulación y validación experimental con un prototipo físico.

El proyecto utiliza:
- **Python (Jupyter Notebook)** para el cálculo de la **cinemática directa (FK)** y la **cinemática inversa (IK)**.
- **Arduino** para el control de tres actuadores (dos articulaciones revolutas y una prismática).
- **GIF(s) de evidencia** que muestran la ejecución del Notebook y el movimiento real del robot.

---

## 1. Descripción del proyecto

El proyecto implementa la **cinemática directa e inversa** de un robot **SCARA RRP** de **3 grados de libertad**, compuesto por:

- Dos articulaciones **revolutas**:  
  - \(q_1\): rotación de la base.  
  - \(q_2\): rotación del segundo eslabón en el plano XY.
- Una articulación **prismática**:  
  - \(d_3\): desplazamiento vertical del efector final sobre el eje Z.

El modelo cinemático se basa en el **método de Denavit–Hartenberg (DH)**, permitiendo describir la relación entre el espacio articular y el espacio cartesiano.

---

## 2. Cinemática directa (Forward Kinematics – FK)

La cinemática directa calcula la **posición cartesiana del efector final** \((x, y, z)\) a partir de las variables articulares \((q_1, q_2, d_3)\).

Flujo de la cinemática directa:

1. El usuario introduce valores articulares:
   - \(q_1, q_2\) en grados.
   - \(d_3\) en milímetros.
2. El Notebook convierte las variables a radianes y metros.
3. Se definen los parámetros DH del robot.
4. Se calculan las matrices homogéneas individuales:
   - \(A_1\), \(A_2\), \(A_3\).
5. Se obtiene la matriz homogénea total:
   \[
   T = A_1 \cdot A_2 \cdot A_3
   \]
6. A partir de \(T\) se extrae la posición del efector final \((x, y, z)\).
7. Los valores articulares se envían al Arduino vía comunicación serial.
8. El Arduino acciona los servomotores y el actuador lineal, reproduciendo el movimiento físico del robot.

---

## 3. Cinemática inversa (Inverse Kinematics – IK)

La cinemática inversa permite calcular las **variables articulares necesarias** para que el efector final alcance una posición cartesiana deseada \((x, y, z)\).

Flujo de la cinemática inversa:

1. El usuario define una posición objetivo del efector final:
   - Coordenadas \((x, y, z)\) dentro del espacio de trabajo del robot.
2. El Notebook verifica que el punto sea **alcanzable** (condición de alcance geométrico).
3. Se resuelve analíticamente la cinemática inversa:
   - Cálculo de \(q_2\) usando la ley de cosenos.
   - Obtención de \(q_1\) a partir de relaciones trigonométricas en el plano XY.
   - Determinación de \(d_3\) a partir de la coordenada Z.
4. Se consideran los límites articulares físicos del robot.
5. Se selecciona la solución válida (configuración del codo).
6. Los valores calculados \((q_1, q_2, d_3)\) se envían al Arduino.
7. El robot se desplaza automáticamente hasta la posición cartesiana solicitada.
8. Se valida el resultado comparando:
   - La posición deseada.
   - La posición obtenida mediante cinemática directa.

---

## 4. Flujo general del sistema

1. Selección del modo de operación:
   - **Cinemática directa** (entrada articular).
   - **Cinemática inversa** (entrada cartesiana).
2. Cálculo cinemático en Python (FK o IK).
3. Visualización de resultados:
   - Variables articulares.
   - Posición cartesiana.
   - Matrices homogéneas.
4. Envío de datos al Arduino por puerto serial.
5. Movimiento del robot SCARA físico.
6. Generación de **GIF de evidencia** del proceso completo.

---

## 5. Estructura del repositorio

```text
.
├─ scara_direct_kinematics.ipynb    # Notebook de cinemática directa
├─ scara_inverse_kinematics.ipynb   # Notebook de cinemática inversa
├─ arduino_scara.ino                # Código de Arduino
├─ media/
│  └─ scara_evidencia.gif           # GIF de evidencia experimental
└─ README.md                        # Este documento
6. Requerimientos
Python
Python 3.10 – 3.12

Instalar dependencias:

bash
Copiar código
pip install numpy pyserial matplotlib imageio
Arduino
Arduino IDE

Librería Servo.h (incluida por defecto)

Comunicación serial configurada a 115200 baud

▶️ Ejecución
1️⃣ Ejecutar los Notebooks
Abrir Jupyter Notebook:

bash
Copiar código
jupyter notebook
Cargar:

scara_direct_kinematics.ipynb para cinemática directa.

scara_inverse_kinematics.ipynb para cinemática inversa.

Pasos generales:

Seleccionar el puerto serial correspondiente.

Elegir el modo de operación (FK o IK).

Ingresar variables articulares o coordenadas cartesianas.

Ejecutar el cálculo cinemático.

Enviar datos al Arduino.

Generar el GIF de evidencia (automático).

2️⃣ Cargar el código en Arduino
Subir el archivo:

text
Copiar código
arduino_scara.ino
El Arduino recibe por serial:

text
Copiar código
q1_rad, q2_rad, d3_m, gripper
y controla en tiempo real:

Los servomotores de las articulaciones R.

El actuador prismático del eje Z.

El efector final.

7. Evidencia experimental
El GIF de evidencia se encuentra en:

text
Copiar código
/media/scara_evidencia.gif
Incluye:

Ejecución de los Notebooks (FK e IK).

Visualización del cálculo de 
(
𝑥
,
𝑦
,
𝑧
)
(x,y,z).

Movimiento real del robot SCARA.

Validación experimental del modelo cinemático.

8. Autores
Kevyn David Delgado Gómez

Eduardo Montiel Salazar

Ingeniería Mecatrónica
Proyecto: Cinemática directa e inversa de robot SCARA RRP



