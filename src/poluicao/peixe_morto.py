"""Peixes mortos boiando: dois peixes prateados de barriga para cima na água poluída (sem sangue)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def peixe(x, y, ang, comp):
    L.esfera(comp / 2, (x, y, 0.0), 'metal', escala=(0.36, 1, 0.3))
    L.esfera(comp / 2 * 0.8, (x, y, 0.012), 'parede', escala=(0.22, 0.85, 0.2))
    L.cilindro(0.03, 0.07, (x, y + comp / 2 - 0.01, 0.0), 'metal_escuro', lados=4, r_topo=0, rot=(-90, 0, 0))


def construir():
    peixe(0, 0, 0, 0.32)
    peixe(0.24, 0.1, 0, 0.26)


L.principal(__file__, construir)
