"""Flutuante de bombonas: dois tambores azuis de plástico amarrados sob um tablado de tábuas, boiando no rio."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.12, 0.12):
        L.cilindro(0.09, 0.42, (x, 0.21, 0.02), 'cano', lados=8, rot=(90, 0, 0))   # bombona deitada, meio afundada
    for y in (-0.14, 0.0, 0.14):
        L.caixa((0.42, 0.1, 0.02), (0, y, 0.11), 'madeira')                           # tábuas
    for y in (-0.08, 0.08):
        L.caixa((0.44, 0.015, 0.03), (0, y, 0.085), 'escuro')                        # cordas


L.principal(__file__, construir)
