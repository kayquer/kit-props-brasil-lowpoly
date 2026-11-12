"""Matacão: pedra grande e arredondada de pasto, com musgo no topo e capim no pé."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.32, (0, 0, 0.2), 'pedra', escala=(1.3, 1.0, 0.8))
    L.esfera(0.22, (0.03, 0.05, 0.4), 'musgo', escala=(1.3, 1.0, 0.35))
    L.esfera(0.12, (0.36, -0.15, 0.06), 'concreto_escuro', escala=(1.1, 1, 0.7))
    for (x, y, h) in ((-0.4, -0.1, 0.13), (0.2, -0.3, 0.1), (-0.15, 0.3, 0.12)):
        L.cone(0.045, h, (x, y, 0), 'verde', lados=4)


L.principal(__file__, construir)
