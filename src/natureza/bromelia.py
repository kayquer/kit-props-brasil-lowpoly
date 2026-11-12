"""Bromélia: roseta de folhas largas e duras abertas em volta de um centro vermelho, rente ao chão."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for i in range(6):
        cor = 'verde' if i % 2 else 'musgo'
        L.caixa((0.07, 0.01, 0.17), (0, 0, 0.01), cor, rot=(58, 0, i * 60))
    for i in range(3):
        L.caixa((0.05, 0.01, 0.12), (0, 0, 0.02), 'verde_escuro', rot=(30, 0, i * 120 + 30))
    L.cone(0.04, 0.13, (0, 0, 0.03), 'vermelho', lados=5)


L.principal(__file__, construir)
