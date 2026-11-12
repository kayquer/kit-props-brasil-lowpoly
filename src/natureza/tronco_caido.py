"""Tronco caído: tora deitada na mata com as pontas claras e um cogumelo vermelho em cima."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.08, 0.64, (-0.32, 0, 0.08), 'madeira_escura', lados=6, rot=(0, 90, 0))
    L.cilindro(0.068, 0.012, (-0.326, 0, 0.08), 'creme', lados=6, rot=(0, 90, 0))
    L.cilindro(0.068, 0.012, (0.314, 0, 0.08), 'creme', lados=6, rot=(0, 90, 0))
    L.caixa((0.012, 0.012, 0.04), (0.1, -0.02, 0.15), 'parede')
    L.cone(0.04, 0.035, (0.1, -0.02, 0.185), 'vermelho', lados=6)
    L.cone(0.04, 0.09, (-0.15, -0.1, 0), 'verde', lados=4)


L.principal(__file__, construir)
