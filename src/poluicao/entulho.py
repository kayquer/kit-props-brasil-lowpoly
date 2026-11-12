"""Entulho: monte de tijolos quebrados, areia, pedaço de concreto e uma tábua, restos de obra jogados no terreno."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cone(0.22, 0.14, (0, 0.04, 0), 'areia', lados=6)
    L.esfera(0.09, (0.18, 0.1, 0.05), 'concreto', escala=(1.2, 1, 0.7))
    for (x, y, z, ang) in ((-0.12, -0.12, 0, 20), (0.0, -0.18, 0, -30), (0.1, -0.1, 0.0, 70),
                           (-0.05, -0.06, 0.07, 45), (-0.2, 0.05, 0, -10)):
        L.caixa((0.1, 0.05, 0.05), (x, y, z), 'telhado_vermelho', rot=(0, 0, ang))
    L.caixa((0.4, 0.06, 0.015), (0.05, 0.18, 0.02), 'madeira', rot=(0, -8, 15))


L.principal(__file__, construir)
