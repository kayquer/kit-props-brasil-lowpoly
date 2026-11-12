"""Bicicletário: base de concreto com dois arcos amarelos em U invertido e uma bicicleta vermelha presa."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def arco(x):
    for dy in (-0.12, 0.12):
        L.caixa((0.03, 0.03, 0.3), (x, dy, 0.03), 'amarelo')
    L.caixa((0.03, 0.27, 0.03), (x, 0, 0.33), 'amarelo')


def construir():
    L.caixa((0.7, 0.4, 0.03), (0, 0, 0), 'concreto')
    arco(-0.18)
    arco(0.18)
    for y in (-0.14, 0.14):
        L.cilindro(0.1, 0.02, (-0.06, y, 0.13), 'escuro', lados=6, rot=(0, 90, 0))
    L.caixa((0.02, 0.3, 0.025), (-0.05, 0, 0.17), 'vermelho', rot=(0, 0, 0))
    L.caixa((0.02, 0.025, 0.12), (-0.05, 0.05, 0.17), 'vermelho', rot=(-20, 0, 0))


L.principal(__file__, construir)
