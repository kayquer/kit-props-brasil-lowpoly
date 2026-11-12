"""Canoa de madeira de pescador boiando: casco pontudo em duas camadas, dois bancos e o remo apoiado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def casco(meia, larg, z, h, cor):
    """Contorno pontudo nas duas pontas (ao longo de Y, 8 pontos), extrudado de z até z + h."""
    pts = [(0, -meia), (larg * 0.75, -meia * 0.55), (larg, 0), (larg * 0.75, meia * 0.55),
           (0, meia), (-larg * 0.75, meia * 0.55), (-larg, 0), (-larg * 0.75, -meia * 0.55)]
    L.prisma(pts, h, (0, 0, z), cor, eixo='Z')


def construir():
    casco(0.6, 0.12, -0.02, 0.06, 'madeira_escura')
    casco(0.66, 0.16, 0.04, 0.05, 'madeira')
    casco(0.56, 0.12, 0.05, 0.045, 'madeira_escura')
    L.caixa((0.26, 0.05, 0.015), (0, -0.24, 0.085), 'madeira')
    L.caixa((0.26, 0.05, 0.015), (0, 0.22, 0.085), 'madeira')
    L.cano((-0.1, -0.35, 0.11), (0.1, 0.25, 0.13), 0.01, 'madeira_escura', lados=4)
    L.caixa((0.06, 0.14, 0.01), (0.12, 0.31, 0.12), 'madeira_escura', rot=(0, 0, -18))


L.principal(__file__, construir)
