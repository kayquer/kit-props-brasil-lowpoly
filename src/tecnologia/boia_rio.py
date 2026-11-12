"""Boia de monitoramento do rio: flutuador amarelo com mastro, plaquinha solar, sensor e luz vermelha."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.16, 0.07, (0, 0, -0.02), 'amarelo', lados=8, r_topo=0.18)
    L.cilindro(0.15, 0.02, (0, 0, 0.05), 'laranja', lados=8)
    L.cilindro(0.06, 0.12, (0, 0, 0.07), 'amarelo', lados=6, r_topo=0.04)
    L.cilindro(0.012, 0.25, (0, 0, 0.19), 'metal', lados=4)
    L.caixa((0.14, 0.1, 0.012), (0, 0, 0.35), 'painel_solar', rot=(-25, 0, 0))
    L.caixa((0.05, 0.04, 0.04), (0.05, 0, 0.29), 'metal_escuro')
    L.cilindro(0.025, 0.05, (0, 0, 0.44), 'vermelho', lados=5)


L.principal(__file__, construir)
