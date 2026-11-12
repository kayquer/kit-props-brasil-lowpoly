"""Tambor enferrujado: barril de metal velho largado, vazando uma poça escura no chão."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.2, (0.08, -0.12, 0.0), 'esgoto', escala=(1.3, 1, 0.05))
    L.cilindro(0.13, 0.34, (0, 0, 0), 'ferrugem', lados=8)
    L.cilindro(0.135, 0.025, (0, 0, 0.11), 'madeira_escura', lados=8)
    L.cilindro(0.135, 0.025, (0, 0, 0.23), 'madeira_escura', lados=8)
    L.cilindro(0.12, 0.012, (0, 0, 0.34), 'metal_escuro', lados=8)


L.principal(__file__, construir)
