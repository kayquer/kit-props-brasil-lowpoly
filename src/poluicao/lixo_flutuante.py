"""Lixo boiando no rio: garrafas PET e sacolas plásticas juntas na superfície da água."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    garrafas = ((-0.15, 0.0, 10), (0.05, 0.08, -35), (0.12, -0.1, 60), (-0.05, -0.14, -80))
    for (x, y, ang) in garrafas:
        L.cilindro(0.028, 0.14, (x, y, 0.0), 'vidro', lados=5, rot=(0, 90, ang))
    L.caixa((0.03, 0.03, 0.03), (-0.15 + 0.15, 0.025, -0.01), 'cano', rot=(0, 0, 10))
    L.caixa((0.03, 0.03, 0.03), (0.05 + 0.12, 0.0, -0.01), 'vermelho', rot=(0, 0, -35))
    L.esfera(0.08, (-0.18, 0.14, 0.0), 'branco', escala=(1.2, 1, 0.25))
    L.esfera(0.07, (0.2, 0.12, 0.0), 'lixo_preto', escala=(1, 1.3, 0.25))


L.principal(__file__, construir)
