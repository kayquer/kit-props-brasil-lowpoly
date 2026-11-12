"""Carrinho de supermercado jogado no córrego: cesto de arame meio afundado e inclinado, rodinhas para o alto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    inc = (0, 32, 0)   # tombado de lado, metade dentro da água (z < 0)
    L.prisma([(-0.18, 0), (0.12, 0), (0.18, 0.22), (-0.2, 0.22)], 0.26, (0, 0, -0.12), 'metal', eixo='X', rot=inc)
    L.prisma([(-0.18, 0.221), (0.16, 0.221), (0.16, 0.227), (-0.18, 0.227)], 0.22, (0, 0, -0.12), 'metal_escuro', eixo='X', rot=inc)  # boca do cesto (vão escuro)
    L.cano((-0.04, 0.2, 0.05), (0.15, 0.24, 0.16), 0.012, 'vermelho', lados=4)       # alça
    for y in (-0.14, 0.12):
        L.cilindro(0.025, 0.02, (0.16, y, 0.14), 'escuro', lados=5, rot=(0, 90, 0))  # rodinhas no ar


L.principal(__file__, construir)
