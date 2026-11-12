"""Hidrômetro: caixinha de metal do relógio de água num pé de concreto, com o visor azul na frente e o cano entrando."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.1, 0.08, 0.16), (0, 0, 0), 'concreto')
    L.caixa((0.18, 0.11, 0.13), (0, 0, 0.16), 'metal')
    L.caixa((0.19, 0.12, 0.02), (0, 0, 0.29), 'metal_escuro')
    L.cilindro(0.04, 0.012, (0, -0.055, 0.225), 'agua', lados=6, rot=(90, 0, 0))
    L.cano((0.09, 0, 0.2), (0.2, 0, 0.2), 0.015, 'cano', lados=4)
    L.cano((0.2, 0, 0.2), (0.2, 0, 0.0), 0.015, 'cano', lados=4)


L.principal(__file__, construir)
