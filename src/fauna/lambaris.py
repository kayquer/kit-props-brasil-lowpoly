"""Cardume de lambaris: cinco peixinhos prateados nadando juntos logo abaixo da superfície da água."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, giro) in ((0, -0.12, 0), (0.12, -0.04, 10), (-0.11, -0.02, -8), (0.05, 0.1, 6), (-0.06, 0.13, -12)):
        L.esfera(0.05, (x, y, -0.005), 'prata', escala=(0.45, 1.3, 0.45))
        L.cilindro(0.03, 0.05, (x, y + 0.06, -0.005), 'agua_funda', lados=3, r_topo=0, rot=(-90, 0, giro))


L.principal(__file__, construir)
