"""Cerca de mourões: três estacas de madeira tortas ligadas por dois fios de arame."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, inclina, h) in ((-0.42, 4, 0.34), (0.0, -3, 0.31), (0.42, 2, 0.33)):
        L.caixa((0.05, 0.05, h), (x, 0, 0), 'madeira_escura', rot=(0, inclina, 0))
    for z in (0.14, 0.26):
        L.caixa((0.88, 0.008, 0.008), (0, -0.026, z), 'metal_escuro')


L.principal(__file__, construir)
