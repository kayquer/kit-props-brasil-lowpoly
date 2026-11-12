"""Carrinho de mão de obra: caçamba de metal cheia de areia, roda na frente e os dois cabos para trás."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    # Caçamba: trapézio (mais larga em cima) ao longo de X
    L.prisma([(-0.15, 0.08), (0.12, 0.08), (0.17, 0.2), (-0.2, 0.2)], 0.22, (0, 0, 0), 'cano', eixo='X')
    L.esfera(0.13, (0, -0.02, 0.19), 'areia', escala=(0.75, 1.25, 0.35))
    L.cilindro(0.06, 0.03, (-0.015, -0.21, 0.06), 'escuro', lados=6, rot=(0, 90, 0))     # roda
    for x in (-0.07, 0.07):
        L.cano((x, 0.08, 0.16), (x, 0.32, 0.17), 0.012, 'madeira', lados=4)             # cabos
        L.caixa((0.02, 0.02, 0.09), (x, 0.08, 0), 'metal_escuro')                        # pés


L.principal(__file__, construir)
