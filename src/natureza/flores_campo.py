"""Flores do campo: florzinhas brancas, amarelas e rosas em hastes finas sobre um tufo baixo de folhas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cone(0.1, 0.06, (0, 0, 0), 'verde', lados=5)
    L.cone(0.07, 0.05, (0.12, 0.06, 0), 'folha', lados=5)
    flores = ((0.02, 0.0, 0.2, 'branco'), (-0.08, 0.05, 0.16, 'flor_amarela'), (0.1, -0.05, 0.14, 'rosa'),
              (0.13, 0.08, 0.18, 'branco'), (-0.05, -0.08, 0.12, 'flor_rosa'))
    for (x, y, h, cor) in flores:
        L.caixa((0.008, 0.008, h), (x, y, 0), 'verde_escuro')
        L.caixa((0.045, 0.045, 0.018), (x, y, h), cor, rot=(0, 0, 45))


L.principal(__file__, construir)
