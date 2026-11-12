"""Taboas de brejo: hastes altas com as espigas marrons e folhas compridas, para a beira d'água."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, h, rot) in ((0, 0, 0.46, (0, 0, 0)), (0.08, 0.03, 0.4, (0, 8, 0)),
                           (-0.07, 0.04, 0.38, (0, -8, 0)), (0.02, -0.07, 0.34, (-8, 0, 0))):
        L.cilindro(0.008, h, (x, y, 0), 'verde_escuro', lados=4, rot=rot)
        L.cilindro(0.022, 0.08, (x, y, h - 0.12), 'madeira_escura', lados=5, rot=rot)
    for (x, y, h, cor, rot) in ((0.04, 0.06, 0.36, 'verde', (12, 14, 0)), (-0.05, -0.04, 0.32, 'folha', (-12, -14, 0)),
                                (0.07, -0.05, 0.28, 'verde', (-14, 16, 0)), (-0.08, 0.07, 0.3, 'folha', (14, -16, 0))):
        L.cilindro(0.025, h, (x, y, 0), cor, lados=4, r_topo=0, rot=rot)


L.principal(__file__, construir)
