"""Trapiche: píer pequeno de tábuas que sai da margem para a frente, sobre estacas curtas, para atracar canoas.

A base (y = +0,3) fica na margem e o píer avança 1,4 para a frente (-Y), por cima da água; as estacas vão de
z = 0 (superfície) até o deck, então o mesmo modelo serve na água e numa vitrine no chão."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.38, 1.4, 0.03), (0, -0.4, 0.1), 'madeira')
    for x in (-0.07, 0.07):
        L.caixa((0.012, 1.38, 0.032), (x, -0.4, 0.101), 'madeira_escura')
    for (x, y) in ((-0.17, 0.2), (0.17, 0.2), (-0.17, -0.5), (0.17, -0.5), (-0.17, -1.05), (0.17, -1.05)):
        L.cilindro(0.025, 0.16, (x, y, 0), 'madeira_escura', lados=4)
    L.caixa((0.42, 0.04, 0.04), (0, -1.08, 0.13), 'madeira_escura')


L.principal(__file__, construir)
