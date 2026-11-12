"""Carcaça de carro abandonado: lataria enferrujada sem rodas, janelas vazias, apoiada em blocos de concreto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for y in (-0.15, 0.15):
        L.caixa((0.22, 0.07, 0.07), (0, y, 0), 'concreto_escuro')                      # blocos
    L.caixa((0.28, 0.6, 0.12), (0, 0, 0.07), 'ferrugem')                                # lataria
    L.prisma([(-0.17, 0), (0.15, 0), (0.1, 0.11), (-0.11, 0.11)], 0.26, (0, 0, 0.19), 'ferrugem', eixo='X')  # cabine
    L.caixa((0.27, 0.2, 0.07), (0, -0.01, 0.2), 'escuro')                               # janelas vazias (laterais)
    L.caixa((0.2, 0.012, 0.06), (0, -0.155, 0.215), 'escuro', rot=(-30, 0, 0))         # para-brisa vazio
    for y in (-0.19, 0.19):
        L.caixa((0.3, 0.1, 0.05), (0, y, 0.05), 'escuro')                               # caixas de roda vazias


L.principal(__file__, construir)
