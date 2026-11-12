"""Latões de leite de alumínio num estrado de madeira na beira da estrada, esperando a coleta."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.4, 0.22, 0.04), (0, 0, 0), 'madeira')
    for x in (-0.1, 0.1):
        L.cilindro(0.075, 0.2, (x, 0, 0.04), 'prata', lados=7, r_topo=0.06)
        L.cilindro(0.045, 0.05, (x, 0, 0.24), 'metal', lados=7)


L.principal(__file__, construir)
