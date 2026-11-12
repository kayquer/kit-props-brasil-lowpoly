"""Poste de concreto de rua: pilar afinando para cima, travessa com isoladores e braço com a luminária acesa."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.12, 0.12, 0.05), (0, 0, 0), 'concreto_escuro')
    L.cilindro(0.045, 1.45, (0, 0, 0.05), 'concreto', lados=4, r_topo=0.028, rot=(0, 0, 45))
    L.caixa((0.34, 0.035, 0.035), (0, 0, 1.36), 'concreto')
    for x in (-0.14, 0.14):
        L.caixa((0.03, 0.03, 0.04), (x, 0, 1.395), 'parede')
    L.cano((0, 0, 1.25), (0, -0.32, 1.32), 0.016, 'metal_escuro', lados=4)
    L.caixa((0.08, 0.16, 0.035), (0, -0.36, 1.29), 'metal_escuro')
    L.caixa((0.06, 0.12, 0.01), (0, -0.36, 1.282), 'flor_amarela')


L.principal(__file__, construir)
