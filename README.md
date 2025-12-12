# Robot SCARA RRP – Cinemática directa e inversa y control con Arduino

Repositorio del proyecto de **cinemática directa e inversa y control de un robot SCARA RRP**, desarrollado como parte de la asignatura de Robótica. El proyecto integra modelado matemático, simulación en Python y validación experimental mediante un prototipo físico controlado con Arduino.

El sistema utiliza:
- **Python (Jupyter Notebook)** para el cálculo de la **cinemática directa (FK)** y la **cinemática inversa (IK)**.
- **Arduino** para el control de dos articulaciones revolutas y una articulación prismática.
- **GIF(s) de evidencia** que muestran la ejecución del Notebook y el movimiento real del robot.

---

## 1. Descripción del proyecto

El proyecto implementa la **cinemática directa e inversa** de un robot **SCARA RRP** de **3 grados de libertad**, compuesto por:

- Dos articulaciones **revolutas**:
  - q1: rotación de la base.
  - q2: rotación del segundo eslabón en el plano XY.
- Una articulación **prismática**:
  - d3: desplazamiento vertical del efector final sobre el eje Z.

El modelo cinemático del robot se desarrolla utilizando el **método de Denavit–Hartenberg (DH)**, lo que permite describir de forma sistemática la relación entre el espacio articular y el espacio cartesiano del efector final.

---

## 2. Cinemática directa (Forward Kinematics – FK)

La cinemática directa permite calcular la **posición del efector final (x, y, z)** a partir de las variables articulares **q1, q2 y d3**.

Flujo de la cinemática directa:

1. El usuario introduce los valores articulares:
   - q1 y q2 en grados.
   - d3 en milímetros.
2. El Notebook convierte los valores a radianes y metros.
3. Se definen los parámetros DH del robot.
4. Se calculan las matrices homogéneas individuales:
   - A1
   - A2
   - A3
5. Se obtiene la matriz homogénea total mediante el producto matricial:

T = A1 · A2 · A3

markdown
Copiar código

6. A partir de la matriz T se extrae la posición del efector final:
- x
- y
- z
7. Los valores articulares se envían al Arduino mediante comunicación serial.
8. El Arduino mapea estos valores a los actuadores físicos y mueve el robot.
9. Se genera evidencia visual del proceso mediante un GIF.

---

## 3. Cinemática inversa (Inverse Kinematics – IK)

La cinemática inversa permite calcular las **variables articulares necesarias** para que el efector final alcance una **posición cartesiana deseada (x, y, z)**.

Flujo de la cinemática inversa:

1. El usuario introduce una posición objetivo del efector final:
- Coordenadas x, y y z.
2. El Notebook verifica que el punto se encuentre dentro del **espacio de trabajo del robot**.
3. Se resuelve la cinemática inversa de forma analítica:
- Cálculo de q2 mediante relaciones geométricas (ley de cosenos).
- Obtención de q1 a partir de relaciones trigonométricas en el plano XY.
- Determinación de d3 directamente a partir de la coordenada Z.
4. Se consideran los **límites articulares físicos** del robot.
5. Se selecciona la solución válida (configuración alcanzable).
6. Los valores calculados de q1, q2 y d3 se envían al Arduino.
7. El robot se mueve automáticamente hasta la posición deseada.
8. Se valida el resultado aplicando cinemática directa a los valores obtenidos y comparando la posición final con la posición objetivo.

---

## 4. Flujo general del sistema

1. Selección del modo de operación:
- Cinemática directa (entrada articular).
- Cinemática inversa (entrada cartesiana).
2. Cálculo cinemático en Python (FK o IK).
3. Visualización de resultados:
- Variables articulares.
- Posición cartesiana del efector final.
- Matrices homogéneas.
4. Envío de datos al Arduino por puerto serial.
5. Movimiento del robot SCARA físico.
6. Generación automática de GIF(s) de evidencia experimental.

---

## 5. Estructura del repositorio

.
├─ scara_direct_kinematics.ipynb # Notebook de cinemática directa
├─ scara_inverse_kinematics.ipynb # Notebook de cinemática inversa
├─ arduino_scara.ino # Código de Arduino
├─ media/
│ └─ scara_evidencia.gif # GIF de evidencia experimental
└─ README.md # Este documento

yaml
Copiar código

---

## 6. Requerimientos

### Python
- Python 3.10 – 3.12

Instalar dependencias:

pip install numpy pyserial matplotlib imageio

yaml
Copiar código

### Arduino
- Arduino IDE
- Librería Servo.h (incluida por defecto)
- Puerto serial configurado a 115200 baud

---

## ▶️ Ejecución

### 1️⃣ Ejecutar los Notebooks

Abrir Jupyter Notebook:

jupyter notebook

yaml
Copiar código

Cargar:
- scara_direct_kinematics.ipynb para cinemática directa.
- scara_inverse_kinematics.ipynb para cinemática inversa.

Pasos generales:
- Seleccionar el puerto serial correspondiente.
- Elegir el modo de operación (FK o IK).
- Ingresar variables articulares o coordenadas cartesianas.
- Ejecutar el cálculo cinemático.
- Enviar los datos al Arduino.
- Generar automáticamente el GIF de evidencia.

---

### 2️⃣ Cargar el código en Arduino

Subir el archivo:

arduino_scara.ino

yaml
Copiar código

El Arduino recibe por comunicación serial:

q1_rad, q2_rad, d3_m, gripper

yaml
Copiar código

y controla en tiempo real:
- Los servomotores de las articulaciones revolutas.
- El actuador prismático del eje Z.
- El efector final.

---

## 7. Evidencia experimental

El GIF de evidencia se encuentra en:

/media/scara_evidencia.gif

yaml
Copiar código

Incluye:
- Ejecución de los Notebooks de cinemática directa e inversa.
- Visualización del cálculo de la posición (x, y, z).
- Movimiento real del robot SCARA.
- Validación experimental del modelo cinemático.

---

## 8. Autores

- **Kevyn David Delgado Gómez**
- **Eduardo Montiel Salazar**

Ingeniería Meccatrónica  
Proyecto: *Cinemática directa e inversa de robot SCARA RRP*
