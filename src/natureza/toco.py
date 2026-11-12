"""Toco de árvore cortada: tronco baixo com o topo claro dos anéis e duas raízes saindo do chão."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.12, 0.15, (0, 0, 0), 'madeira', lados=7, r_topo=0.1)
    L.cilindro(0.09, 0.012, (0, 0, 0.15), 'creme', lados=7)
    L.cilindro(0.045, 0.014, (0, 0, 0.152), 'cavaco', lados=7)
    L.caixa((0.14, 0.05, 0.04), (0.13, 0.02, 0), 'madeira_escura', rot=(0, 0, 20))
    L.caixa((0.05, 0.12, 0.035), (-0.05, -0.12, 0), 'madeira_escura', rot=(0, 0, 15))


L.principal(__file__, construir)
