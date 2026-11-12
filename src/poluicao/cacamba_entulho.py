"""Caçamba de entulho amarela, pequena, transbordando de tijolos, restos de concreto e tábuas quebradas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    # Caçamba: trapézio ao longo de X (mais curta embaixo), boca para cima
    L.prisma([(-0.17, 0.02), (0.17, 0.02), (0.22, 0.22), (-0.22, 0.22)], 0.36, (0, 0, 0), 'amarelo', eixo='X')
    for x in (-0.12, 0.12):
        L.caixa((0.04, 0.46, 0.03), (x, 0, 0), 'metal_escuro')                      # trilhos de baixo
    L.esfera(0.17, (0.0, 0.0, 0.2), 'concreto_escuro', escala=(1.05, 1.3, 0.45))   # entulho transbordando
    L.esfera(0.1, (0.08, -0.08, 0.25), 'tijolo', escala=(1, 1, 0.6))
    L.caixa((0.04, 0.3, 0.02), (-0.08, 0.02, 0.26), 'madeira', rot=(14, 0, 25))    # tábua quebrada


L.principal(__file__, construir)
