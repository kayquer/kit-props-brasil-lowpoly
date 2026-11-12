"""Vaca malhada de pasto: corpo branco com manchas pretas, focinho rosa e chifres curtos, de frente para a câmera."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y) in ((-0.07, -0.13), (0.07, -0.13), (-0.07, 0.14), (0.07, 0.14)):
        L.caixa((0.05, 0.05, 0.17), (x, y, 0), 'branco')
    L.caixa((0.21, 0.4, 0.17), (0, 0.01, 0.16), 'branco')
    L.caixa((0.012, 0.14, 0.1), (0.105, 0.06, 0.2), 'escuro')
    L.caixa((0.012, 0.1, 0.08), (-0.105, -0.06, 0.22), 'escuro')
    L.caixa((0.13, 0.13, 0.13), (0, -0.24, 0.24), 'branco')
    L.caixa((0.11, 0.05, 0.07), (0, -0.32, 0.24), 'rosa')
    for x in (-0.05, 0.05):
        L.cone(0.015, 0.06, (x, -0.22, 0.37), 'creme', lados=4)
    L.cano((0, 0.21, 0.3), (0.02, 0.24, 0.15), 0.01, 'escuro', lados=3)


L.principal(__file__, construir)
