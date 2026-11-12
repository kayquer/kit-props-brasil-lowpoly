"""Carrinho de pipoca: caixa vermelha com a vitrine de vidro, duas rodas, guidão e guarda-sol vermelho e branco."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.16, 0.16):
        L.cilindro(0.065, 0.025, (x, 0.02, 0.065), 'escuro', lados=6, rot=(0, 90, 0))
    L.caixa((0.3, 0.2, 0.2), (0, 0, 0.07), 'vermelho')
    L.caixa((0.28, 0.18, 0.15), (0, 0, 0.27), 'vidro')
    L.caixa((0.31, 0.21, 0.02), (0, 0, 0.42), 'parede')
    L.cano((0, 0.1, 0.22), (0, 0.24, 0.3), 0.01, 'metal_escuro', lados=3)
    L.cano((0.1, 0.05, 0.44), (0.1, 0.05, 0.72), 0.008, 'metal', lados=3)
    L.cone(0.24, 0.09, (0.1, 0.05, 0.68), 'vermelho', lados=6)
    L.cone(0.1, 0.04, (0.1, 0.05, 0.73), 'branco', lados=6)


L.principal(__file__, construir)
