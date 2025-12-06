import numpy as np

"""
Módulo de cinemática directa para un robot SCARA RRP de 3 GDL.

Convención:
- q1, q2 en radianes
- d3 en metros
- Salida (x, y, z) en metros
"""

# ==========================
# Parámetros geométricos
# (ajustados a tu robot)
# ==========================
L1 = 0.10    # [m] longitud del primer eslabón
L2 = 0.15    # [m] longitud del segundo eslabón
D0 = 0.012   # [m] altura desde la base hasta la articulación 1

# Límites articulares (en radianes y metros)
QLIM_1 = (-np.pi/2, np.pi/2)   # q1: -90° a +90°
QLIM_2 = (-np.pi/2, np.pi/2)   # q2: -90° a +90°
QLIM_3 = (0.0, 0.06)         # d3: -5 cm a +10 cm (ajusta según tu actuador)


def dh(a, alpha, d, theta):
    """
    Matriz de transformación homogénea usando parámetros DH estándar.
    """
    ca, sa = np.cos(alpha), np.sin(alpha)
    ct, st = np.cos(theta), np.sin(theta)

    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0.0,     sa,      ca,      d],
        [0.0,   0.0,    0.0,    1.0]
    ])


def fk_scara(q1_rad, q2_rad, d3_m):
    """
    Cinemática directa del SCARA RRP usando DH.

    Entradas:
        q1_rad: ángulo de la primera articulación [rad]
        q2_rad: ángulo de la segunda articulación [rad]
        d3_m: desplazamiento de la articulación prismática [m]

    Salidas:
        dict con:
            - A1, A2, A3: matrices homogéneas individuales (4x4)
            - T: matriz homogénea total (4x4)
            - x, y, z: posición del efector final [m]
    """

    # Parámetros DH según tu definición con roboticstoolbox:
    # L1 = RevoluteDH(d=0.012, a=0.10, alpha=0.0)
    # L2 = RevoluteDH(d=0.0,   a=0.15, alpha=pi)
    # L3 = PrismaticDH(theta=0.0, a=0.0, alpha=0.0)

    a1, alpha1, d1, theta1 = L1, 0.0,  D0,  q1_rad
    a2, alpha2, d2, theta2 = L2, np.pi, 0.0, q2_rad
    a3, alpha3, d3, theta3 = 0.0, 0.0, d3_m, 0.0   # prismatico: d = d3_m

    A1 = dh(a1, alpha1, d1, theta1)
    A2 = dh(a2, alpha2, d2, theta2)
    A3 = dh(a3, alpha3, d3, theta3)

    T = A1 @ A2 @ A3

    x, y, z = T[0, 3], T[1, 3], T[2, 3]

    return {
        "A1": A1,
        "A2": A2,
        "A3": A3,
        "T": T,
        "x": x,
        "y": y,
        "z": z
    }


def fk_scara_planar(q1_rad, q2_rad, d3_m):
    """
    Versión simplificada en el plano XY (útil para área de trabajo).

    x = L1 cos(q1) + L2 cos(q1 + q2)
    y = L1 sin(q1) + L2 sin(q1 + q2)
    z = D0 + d3
    """
    x = L1 * np.cos(q1_rad) + L2 * np.cos(q1_rad + q2_rad)
    y = L1 * np.sin(q1_rad) + L2 * np.sin(q1_rad + q2_rad)
    z = D0 - d3_m
    return x, y, z


def check_joint_limits(q1_rad, q2_rad, d3_m):
    """
    Verifica si (q1, q2, d3) están dentro de los límites físicos definidos.
    """
    ok1 = QLIM_1[0] <= q1_rad <= QLIM_1[1]
    ok2 = QLIM_2[0] <= q2_rad <= QLIM_2[1]
    ok3 = QLIM_3[0] <= d3_m    <= QLIM_3[1]
    return ok1 and ok2 and ok3


def create_rtb_robot():
    """
    (Opcional) Crea el robot en formato roboticstoolbox (DHRobot),
    compatible con el código que ya habías usado.
    """
    import roboticstoolbox as rtb

    L1_link = rtb.RevoluteDH(
        d=D0,
        a=L1,
        alpha=0.0,
        qlim=QLIM_1
    )

    L2_link = rtb.RevoluteDH(
        d=0.0,
        a=L2,
        alpha=np.pi,
        qlim=QLIM_2
    )

    L3_link = rtb.PrismaticDH(
        theta=0.0,
        a=0.0,
        alpha=0.0,
        qlim=QLIM_3
    )

    robot = rtb.DHRobot([L1_link, L2_link, L3_link], name="SCARA_REAL")
    return robot
