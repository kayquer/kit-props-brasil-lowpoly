"""Sofá velho abandonado na calçada: estofado marrom desbotado, almofada torta e um rasgo mostrando a espuma amarela."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.5, 0.24, 0.1), (0, 0, 0.02), 'marrom')                         # assento
    L.caixa((0.5, 0.07, 0.24), (0, 0.1, 0.02), 'marrom', rot=(-8, 0, 0))     # encosto
    for x in (-0.23, 0.23):
        L.caixa((0.05, 0.24, 0.17), (x, 0, 0.02), 'madeira_escura')           # braços
    L.caixa((0.2, 0.18, 0.05), (-0.1, -0.01, 0.12), 'capivara', rot=(0, 6, 4))  # almofada torta
    L.caixa((0.1, 0.012, 0.06), (0.12, -0.121, 0.05), 'amarelo', rot=(0, 0, 0))  # rasgo (espuma)


L.principal(__file__, construir)
