"""Canteiro de horta: caixa de madeira com terra, uma fileira de alfaces e outra de cenouras."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.tanque(0.8, 0.45, 0.13, (0, 0, 0), cor_agua='terra', cor='madeira', parede=0.04, nivel=0.025)
    for i in range(3):
        L.esfera(0.06, (-0.24 + i * 0.24, -0.09, 0.13), 'folha', escala=(1, 1, 0.7))
    for i in range(4):
        x = -0.27 + i * 0.18
        L.cone(0.03, 0.1, (x, 0.1, 0.105), 'verde', lados=4)


L.principal(__file__, construir)
