"""Poço caipira de tijolo: boca redonda com água escura, sarilho com corda entre dois paus, telhadinho e o balde."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.17, 0.18, (0, 0, 0), 'tijolo', lados=8)
    L.cilindro(0.13, 0.181, (0, 0, 0.001), 'agua_funda', lados=8)          # água lá dentro (só o topo aparece)
    for x in (-0.19, 0.19):
        L.caixa((0.03, 0.03, 0.44), (x, 0, 0), 'madeira')
    L.cano((-0.19, 0, 0.33), (0.19, 0, 0.33), 0.022, 'madeira_escura', lados=4)  # sarilho
    L.cano((0.0, 0, 0.33), (0.0, 0, 0.24), 0.005, 'cana_seca', lados=3)        # corda
    L.prisma([(-0.15, 0), (0.15, 0), (0, 0.1)], 0.48, (0, 0, 0.44), 'telhado_vermelho', eixo='X')
    L.cilindro(0.04, 0.06, (0, 0, 0.18), 'metal', lados=5, r_topo=0.05)        # balde


L.principal(__file__, construir)
