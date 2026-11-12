"""Sacos de lixo: três sacos pretos amarrados, largados juntos na calçada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, r, k) in ((0, 0, 0.11, 1.0), (0.17, 0.05, 0.09, 0.9), (-0.12, 0.1, 0.08, 0.85)):
        L.esfera(r, (x, y, r * 0.85), 'lixo_preto', escala=(1, 0.95, 0.9 * k))
        L.cone(0.025, 0.06, (x, y, r * 1.6), 'lixo_preto', lados=4)


L.principal(__file__, construir)
