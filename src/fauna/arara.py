"""Arara-vermelha pousada num galho seco baixo: corpo vermelho, asas azuis e a cauda comprida caindo para trás."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cano((-0.14, 0.04, 0), (-0.08, 0.04, 0.3), 0.022, 'madeira_escura', lados=4)   # galho seco
    L.cano((-0.12, 0.04, 0.27), (0.14, 0.04, 0.33), 0.018, 'madeira_escura', lados=4)
    L.esfera(0.065, (0.02, 0.03, 0.4), 'vermelho', escala=(0.85, 1, 1.25))           # corpo
    L.esfera(0.042, (0.02, -0.01, 0.5), 'vermelho')                                  # cabeça
    L.cone(0.02, 0.05, (0.02, -0.05, 0.48), 'escuro', lados=4)                       # bico curvo
    for x in (-0.045, 0.085):
        L.caixa((0.02, 0.09, 0.1), (x, 0.04, 0.35), 'azul_arara', rot=(-15, 0, 0))  # asas
    L.caixa((0.04, 0.02, 0.24), (0.02, 0.1, 0.1), 'vermelho', rot=(-12, 0, 0))       # cauda
    L.caixa((0.03, 0.02, 0.14), (0.02, 0.115, 0.06), 'azul_arara', rot=(-12, 0, 0))


L.principal(__file__, construir)
