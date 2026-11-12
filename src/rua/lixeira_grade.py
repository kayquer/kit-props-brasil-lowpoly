"""Lixeira de grade: cesto aberto de barras de metal no topo de um poste, com um saco de lixo dentro."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.035, 0.035, 0.62), (0, 0.12, 0), 'metal_escuro')
    L.caixa((0.24, 0.22, 0.012), (0, 0, 0.6), 'metal_escuro')
    for (x, y) in ((-0.11, -0.1), (0.11, -0.1), (-0.11, 0.1), (0.11, 0.1), (0, -0.1), (-0.11, 0)):
        L.caixa((0.014, 0.014, 0.17), (x, y, 0.6), 'metal')
    L.caixa((0.24, 0.014, 0.014), (0, -0.1, 0.76), 'metal')
    L.caixa((0.014, 0.22, 0.014), (-0.11, 0, 0.76), 'metal')
    L.esfera(0.09, (0.01, 0.01, 0.68), 'lixo_preto', escala=(1, 1, 0.8))


L.principal(__file__, construir)
