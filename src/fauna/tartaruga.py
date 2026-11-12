"""Tartaruga de rio: casco abaulado verde-escuro com a borda clara, cabeça e quatro patas para fora."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y) in ((-0.09, -0.07), (0.09, -0.07), (-0.08, 0.08), (0.08, 0.08)):
        L.caixa((0.06, 0.05, 0.025), (x, y, 0), 'musgo', rot=(0, 0, 30 if x * y > 0 else -30))
    L.cilindro(0.115, 0.025, (0, 0, 0.015), 'musgo', lados=6)
    L.cupula(0.105, (0, 0, 0.04), 'verde_escuro', lados=6, aneis=2)
    L.esfera(0.035, (0, -0.14, 0.04), 'musgo', escala=(1, 1.2, 0.9))


L.principal(__file__, construir)
