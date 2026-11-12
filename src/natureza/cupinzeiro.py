"""Cupinzeiro: montinho de terra vermelha de pasto, alto e irregular, com uma torre menor ao lado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.17, 0.3, (0, 0, 0), 'terra_vermelha', lados=6, r_topo=0.08)
    L.esfera(0.09, (0.01, 0, 0.32), 'terra_vermelha', escala=(1, 1, 1.1))
    L.cone(0.09, 0.2, (0.17, -0.06, 0), 'terra', lados=5)
    L.cone(0.05, 0.08, (-0.18, 0.1, 0), 'verde', lados=4)


L.principal(__file__, construir)
