"""Tamanduá-bandeira: corpo acinzentado com a faixa preta no ombro, focinho comprido e fino e a cauda enorme de bandeira."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.11, 0.04, 0.1), (0, -0.08, 0), 'escuro')            # patas da frente
    L.caixa((0.11, 0.04, 0.1), (0, 0.1, 0), 'madeira_escura')      # patas de trás
    L.esfera(0.11, (0, 0.01, 0.17), 'concreto_escuro', escala=(0.75, 1.5, 0.8))
    L.caixa((0.17, 0.05, 0.02), (0, -0.04, 0.2), 'escuro', rot=(0, 0, 25))       # faixa do ombro
    L.cilindro(0.04, 0.22, (0, -0.13, 0.17), 'concreto_escuro', lados=4, r_topo=0.012, rot=(98, 0, 0))  # focinho
    # Cauda grande e peluda de bandeira, arrastando para trás quase rente ao chão (perfil (y, z) achatado)
    L.prisma([(0, 0.06), (0.16, 0.02), (0.34, 0.03), (0.36, 0.12), (0.14, 0.2)], 0.07, (0, 0.12, 0.0), 'madeira_escura', eixo='X')


L.principal(__file__, construir)
