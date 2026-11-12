"""Colmeia de abelhas: duas caixas brancas empilhadas com tampa azul e entrada escura, num cavalete de madeira."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.09, 0.09):
        L.caixa((0.04, 0.2, 0.12), (x, 0, 0), 'madeira_escura')
    L.caixa((0.24, 0.2, 0.11), (0, 0, 0.12), 'branco')
    L.caixa((0.24, 0.2, 0.1), (0, 0, 0.235), 'parede')
    L.caixa((0.27, 0.23, 0.03), (0, 0, 0.335), 'telhado_azul')
    L.caixa((0.12, 0.01, 0.018), (0, -0.1, 0.13), 'escuro')


L.principal(__file__, construir)
