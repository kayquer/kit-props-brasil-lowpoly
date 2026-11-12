"""Cata-vento de bombear água: torre fina de metal com a roda de pás e o leme no alto, e a caixinha d'água no pé."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    topo = (0, 0, 1.12)
    for (x, y) in ((-0.13, -0.13), (0.13, -0.13), (0.13, 0.13), (-0.13, 0.13)):
        L.cano((x, y, 0), (x * 0.15, y * 0.15, topo[2]), 0.012, 'metal_escuro', lados=3)
    L.caixa((0.2, 0.2, 0.015), (0, 0, 0.45), 'metal_escuro')                    # travessa
    L.cilindro(0.035, 0.08, (0, 0.04, topo[2] + 0.06), 'metal_escuro', lados=5, rot=(90, 0, 0))  # cubo
    # Roda de pás (estática), de frente para -Y
    # (a caixa gira em torno da base: a base fica a meio comprimento do cubo, do lado oposto à ponta)
    cubo_z = topo[2] + 0.06
    for ang in (0, 45, 90, 135):
        a = math.radians(ang)
        L.caixa((0.05, 0.012, 0.44), (-0.22 * math.sin(a), -0.05, cubo_z - 0.22 * math.cos(a)), 'metal', rot=(0, ang, 0))
    L.caixa((0.012, 0.22, 0.12), (0, 0.2, topo[2] + 0.02), 'vermelho')            # leme
    L.cilindro(0.1, 0.12, (0.26, -0.14, 0), 'cano', lados=5)                       # caixinha d'água


L.principal(__file__, construir)
