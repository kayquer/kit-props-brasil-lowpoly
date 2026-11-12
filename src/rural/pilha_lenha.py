"""Pilha de lenha de eucalipto cortada e arrumada entre duas estacas, toras finas deitadas em três camadas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    r = 0.045
    toras = [(-0.1, r), (0, r), (0.1, r), (-0.05, r * 2.7), (0.05, r * 2.7), (0, r * 4.4)]
    for i, (y, z) in enumerate(toras):
        L.cilindro(r, 0.4, (-0.2, y, z), 'madeira_clara' if i % 2 else 'madeira', lados=5, rot=(0, 90, 0))
    for y in (-0.16, 0.16):
        L.caixa((0.025, 0.025, 0.24), (0.0, y, 0), 'madeira_escura')


L.principal(__file__, construir)
