"""Tucano: ave preta de peito amarelo pousada num toco baixo, com o bico laranja enorme apontando para a frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.06, 0.22, (0, 0.02, 0), 'madeira', lados=5)
    L.cilindro(0.05, 0.01, (0, 0.02, 0.22), 'madeira_clara', lados=5)
    L.esfera(0.08, (0, 0.03, 0.31), 'escuro', escala=(0.8, 1.1, 1.05))     # corpo
    L.caixa((0.08, 0.02, 0.07), (0, -0.045, 0.3), 'amarelo')                  # peito
    L.esfera(0.05, (0, -0.02, 0.4), 'escuro', escala=(0.9, 1, 0.95))        # cabeça
    L.cilindro(0.035, 0.17, (0, -0.06, 0.4), 'laranja', lados=4, r_topo=0.008, rot=(90, 0, 0))  # bico
    L.caixa((0.05, 0.12, 0.02), (0, 0.13, 0.26), 'escuro', rot=(-35, 0, 0))   # cauda


L.principal(__file__, construir)
