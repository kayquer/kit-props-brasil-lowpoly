"""Manilha de esgoto: cano de concreto saindo do barranco e despejando um fio de água escura para a frente.

A boca da manilha olha para a frente (-Y): o fio escuro desce até z = 0 e forma uma poça com espuma."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.2, (0, 0.14, 0.08), 'terra', escala=(1.3, 1, 0.8))
    L.cilindro(0.11, 0.3, (0, 0.18, 0.16), 'concreto', lados=8, rot=(90, 0, 0))
    L.cilindro(0.085, 0.01, (0, -0.125, 0.16), 'escuro', lados=8, rot=(90, 0, 0))
    L.caixa((0.08, 0.2, 0.012), (0, -0.2, 0.06), 'esgoto', rot=(-35, 0, 0))
    L.esfera(0.14, (0, -0.38, 0.0), 'esgoto', escala=(1.2, 1, 0.12))
    L.esfera(0.05, (0.06, -0.4, 0.01), 'espuma', escala=(1.2, 1, 0.3))


L.principal(__file__, construir)
