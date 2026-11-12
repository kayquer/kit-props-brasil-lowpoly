"""Capim alto: tufo de folhas finas verde-amareladas, inclinadas para os lados como mato de beira de estrada."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    folhas = ((0, 0, 0.32, 'verde', (0, 0, 0)), (0.05, 0.02, 0.28, 'folha', (0, 18, 0)),
              (-0.05, 0.01, 0.27, 'feno', (0, -20, 0)), (0.0, 0.05, 0.26, 'verde', (18, 0, 0)),
              (0.01, -0.05, 0.25, 'feno', (-18, 0, 0)), (0.06, -0.04, 0.2, 'folha', (-10, 22, 0)),
              (-0.06, -0.04, 0.22, 'verde', (-12, -22, 0)), (-0.04, 0.06, 0.2, 'feno', (15, -15, 0)),
              (0.07, 0.06, 0.18, 'verde', (15, 20, 0)))
    for (x, y, h, cor, rot) in folhas:
        L.cilindro(0.03, h, (x, y, 0), cor, lados=4, r_topo=0, rot=rot)


L.principal(__file__, construir)
