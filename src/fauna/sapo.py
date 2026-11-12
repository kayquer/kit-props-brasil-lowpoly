"""Sapo verde sentado numa pedrinha da margem, com os olhos saltados em cima e as patas dobradas dos lados."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.13, (0, 0.02, 0.03), 'pedra', escala=(1.2, 1, 0.55))
    L.esfera(0.075, (0, 0, 0.13), 'verde_sapo', escala=(1.1, 1.2, 0.7))
    for x in (-0.035, 0.035):
        L.esfera(0.022, (x, -0.04, 0.18), 'amarelo')
    for x in (-0.075, 0.075):
        L.caixa((0.04, 0.09, 0.03), (x, 0.03, 0.09), 'verde_escuro')


L.principal(__file__, construir)
