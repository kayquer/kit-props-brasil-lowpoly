"""Cone de trânsito laranja com faixa branca, sobre a base quadrada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.16, 0.16, 0.02), (0, 0, 0), 'laranja')
    L.cilindro(0.06, 0.24, (0, 0, 0.02), 'laranja', lados=6, r_topo=0.012)
    L.cilindro(0.046, 0.045, (0, 0, 0.1), 'branco', lados=6, r_topo=0.037)


L.principal(__file__, construir)
