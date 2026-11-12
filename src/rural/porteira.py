"""Porteira de fazenda: portão de madeira com quatro ripas e uma diagonal, entre dois mourões grossos."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.42, 0.42):
        L.caixa((0.07, 0.07, 0.46), (x, 0, 0), 'madeira_escura')
    for i in range(4):
        L.caixa((0.76, 0.03, 0.04), (0, 0, 0.06 + i * 0.1), 'madeira')
    ang = math.degrees(math.atan2(0.3, 0.72))
    L.caixa((0.78, 0.03, 0.04), (0, -0.01, 0.2), 'madeira', rot=(0, -ang, 0))


L.principal(__file__, construir)
