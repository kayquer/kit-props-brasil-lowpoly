"""Hidrante de rua: corpo vermelho com tampa amarela e três saídas, sobre uma base de concreto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.09, 0.025, (0, 0, 0), 'concreto', lados=6)
    L.cilindro(0.055, 0.21, (0, 0, 0.025), 'vermelho', lados=6)
    L.cupula(0.06, (0, 0, 0.235), 'amarelo', lados=6, aneis=2)
    for (a, b) in (((0.05, 0, 0.17), (0.1, 0, 0.17)), ((-0.05, 0, 0.17), (-0.1, 0, 0.17)), ((0, -0.05, 0.15), (0, -0.1, 0.15))):
        L.cano(a, b, 0.026, 'vermelho', lados=4)


L.principal(__file__, construir)
