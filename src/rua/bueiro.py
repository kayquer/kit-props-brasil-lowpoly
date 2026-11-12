"""Bueiro: tampa redonda de ferro com grelha de drenagem, rente ao chão num anel de concreto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.17, 0.012, (0, 0, 0), 'concreto', lados=8)
    L.cilindro(0.13, 0.018, (0, 0, 0), 'metal_escuro', lados=8)
    for i in range(3):
        L.caixa((0.2, 0.022, 0.006), (0, -0.06 + i * 0.06, 0.018), 'escuro')


L.principal(__file__, construir)
