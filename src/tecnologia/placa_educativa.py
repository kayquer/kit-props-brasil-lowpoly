"""Placa educativa de beira de rio: quadro de madeira com telhadinho, gota azul e árvore desenhadas (sem letras)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for px in (-0.28, 0.28):
        L.caixa((0.045, 0.045, 0.62), (px, 0.02, 0), 'madeira_escura')
    L.caixa((0.62, 0.035, 0.36), (0, 0.0, 0.22), 'madeira')
    L.placa(0.54, 0.29, (0, -0.018, 0.545), 'parede', 'frente', espessura=0.008)
    L.esfera(0.05, (-0.17, -0.024, 0.37), 'agua_funda', escala=(1, 0.2, 1))
    L.caixa((0.012, 0.006, 0.05), (0.17, -0.024, 0.33), 'madeira_escura')
    L.esfera(0.045, (0.17, -0.024, 0.41), 'verde', escala=(1, 0.2, 1))
    L.placa(0.48, 0.035, (0, -0.023, 0.52), 'telhado_verde', 'frente', espessura=0.006)
    L.placa(0.16, 0.012, (0.0, -0.023, 0.44), 'escuro', 'frente', espessura=0.004)
    L.prisma(((-0.06, 0.0), (0.06, 0.0), (0.0, 0.07)), 0.68, (0, 0.0, 0.58), 'telhado_vermelho', eixo='X')


L.principal(__file__, construir)
