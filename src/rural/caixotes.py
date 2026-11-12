"""Caixotes de madeira empilhados com laranjas e tomates, como os da colheita no sítio."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def caixote(x, y, z, fruta, rot=0):
    L.caixa((0.2, 0.15, 0.11), (x, y, z), 'madeira', rot=(0, 0, rot))
    L.caixa((0.205, 0.155, 0.02), (x, y, z + 0.045), 'madeira_escura', rot=(0, 0, rot))
    if fruta:
        L.caixa((0.18, 0.13, 0.02), (x, y, z + 0.105), fruta, rot=(0, 0, rot))


def construir():
    caixote(-0.11, 0, 0, 'laranja')
    caixote(0.12, 0.02, 0, 'vermelho', rot=8)
    caixote(0, 0.01, 0.11, 'laranja', rot=-6)


L.principal(__file__, construir)
