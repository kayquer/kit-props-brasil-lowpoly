"""Arbustos de canteiro: quatro tufos em verdes variados com algumas flores rosas e amarelas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, r, cor) in ((0, 0, 0.16, 'verde'), (0.22, -0.08, 0.12, 'verde_escuro'), (-0.2, 0.06, 0.13, 'folha'),
                           (0.06, 0.2, 0.11, 'verde_escuro')):
        L.arbusto((x, y, 0), r, cor)
    for (x, y, z, cor) in ((0.04, -0.13, 0.17, 'flor_rosa'), (-0.12, 0.0, 0.2, 'flor_amarela'),
                           (0.22, -0.16, 0.13, 'flor_amarela'), (0.08, 0.14, 0.2, 'flor_rosa')):
        L.caixa((0.045, 0.045, 0.03), (x, y, z), cor, rot=(0, 0, 30))


L.principal(__file__, construir)
