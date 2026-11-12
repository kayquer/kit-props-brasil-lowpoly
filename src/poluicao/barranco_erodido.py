"""Barranco erodido sem mata ciliar: terra vermelha desmoronando para a frente (a água), com raízes expostas e torrões caídos.

A face desmoronada olha para a frente (-Y): o jogo vira a frente para a água."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    # Monte de terra irregular (não um bloco): dois pedaços com perfis tortos, o corte vermelho para a frente
    L.prisma([(0.2, 0), (0.18, 0.12), (0.06, 0.2), (-0.02, 0.16), (-0.06, 0.06), (-0.2, 0)], 0.3,
             (-0.12, 0, 0), 'terra_vermelha', eixo='X')
    L.prisma([(0.2, 0), (0.16, 0.16), (0.02, 0.17), (-0.08, 0.05), (-0.22, 0)], 0.26,
             (0.15, 0.02, 0), 'terra', eixo='X')
    L.esfera(0.09, (-0.12, 0.14, 0.17), 'grama', escala=(1.6, 0.8, 0.35))           # capim que sobrou no alto
    L.esfera(0.08, (0.15, 0.14, 0.15), 'grama', escala=(1.5, 0.8, 0.35))
    for (x, y, z) in ((-0.2, -0.0, 0.15), (0.02, 0.02, 0.15), (0.2, 0.0, 0.13)):
        L.cano((x, y + 0.04, z), (x + 0.03, y - 0.08, z - 0.12), 0.009, 'madeira_escura', lados=3)  # raízes
    L.esfera(0.05, (-0.1, -0.24, 0.02), 'terra_vermelha', escala=(1, 1, 0.6))      # torrões caídos
    L.esfera(0.04, (0.12, -0.26, 0.01), 'terra', escala=(1, 1, 0.6))


L.principal(__file__, construir)
