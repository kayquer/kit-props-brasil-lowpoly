"""Tatu: casco cinza em faixas, cabeça pontuda com orelhinhas para a frente e rabo fino atrás."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.12, 0.04, 0.04), (0, -0.07, 0), 'madeira_escura')
    L.caixa((0.12, 0.04, 0.04), (0, 0.08, 0), 'madeira_escura')
    L.esfera(0.12, (0, 0, 0.09), 'pedra', escala=(0.85, 1.25, 0.75))      # casco
    for y in (-0.05, 0.0, 0.05):
        L.caixa((0.2, 0.018, 0.022), (0, y, 0.165), 'concreto_escuro')     # faixas do casco
    L.cilindro(0.04, 0.12, (0, -0.12, 0.08), 'pedra', lados=4, r_topo=0.012, rot=(100, 0, 0))  # focinho
    for x in (-0.025, 0.025):
        L.caixa((0.02, 0.01, 0.04), (x, -0.13, 0.11), 'concreto_escuro')  # orelhas
    L.cilindro(0.02, 0.12, (0, 0.14, 0.06), 'pedra', lados=4, r_topo=0.004, rot=(-100, 0, 0))  # rabo


L.principal(__file__, construir)
