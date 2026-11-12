"""Espuma de poluição: manchas de espuma branca boiando na água, de detergente e esgoto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, r) in ((0, 0, 0.2), (0.28, 0.08, 0.13), (-0.24, 0.12, 0.12), (0.06, -0.24, 0.11), (-0.16, -0.18, 0.08)):
        L.esfera(r, (x, y, 0.0), 'espuma', escala=(1.2, 1, 0.22))


L.principal(__file__, construir)
