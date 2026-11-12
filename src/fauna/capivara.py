"""Capivara: roedor marrom de corpo arredondado e focinho quadrado, de frente para a câmera."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y) in ((-0.07, -0.1), (0.07, -0.1), (-0.07, 0.12), (0.07, 0.12)):
        L.caixa((0.045, 0.045, 0.08), (x, y, 0), 'madeira_escura')
    L.esfera(0.15, (0, 0.02, 0.17), 'capivara', escala=(0.8, 1.3, 0.75))
    L.caixa((0.12, 0.13, 0.1), (0, -0.2, 0.14), 'capivara')
    L.caixa((0.1, 0.05, 0.07), (0, -0.28, 0.13), 'madeira_escura')
    for x in (-0.04, 0.04):
        L.caixa((0.03, 0.025, 0.03), (x, -0.16, 0.24), 'madeira_escura')


L.principal(__file__, construir)
