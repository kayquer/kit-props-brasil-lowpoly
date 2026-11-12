"""Banco de praça: assento e encosto de ripas de madeira sobre dois pés de ferro escuro com braços."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for px in (-0.3, 0.3):
        L.caixa((0.04, 0.2, 0.17), (px, 0, 0), 'escuro')
        L.caixa((0.04, 0.2, 0.025), (px, -0.005, 0.25), 'escuro')
    for i in range(2):
        L.caixa((0.72, 0.085, 0.02), (0, -0.05 + i * 0.1, 0.17), 'madeira')
    for i in range(2):
        L.caixa((0.72, 0.018, 0.05), (0, 0.1, 0.21 + i * 0.07), 'madeira', rot=(-10, 0, 0))


L.principal(__file__, construir)
