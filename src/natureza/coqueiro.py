"""Coqueiro: tronco fino e curvo em três trechos, coroa de folhas compridas caindo em volta e um cacho de cocos."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    pontos = [(0, 0, 0), (0.05, 0, 0.4), (0.13, 0, 0.78), (0.24, 0, 1.08)]
    for a, b in zip(pontos, pontos[1:]):
        L.cano(a, b, 0.035, 'madeira', lados=5)
    topo = pontos[-1]
    # Folhas: caixas finas e compridas saindo do topo e caindo para fora
    for i in range(6):
        L.caixa((0.08, 0.012, 0.42), topo, 'verde' if i % 2 else 'folha', rot=(105, 0, i * 60 + 15))
    L.esfera(0.06, (topo[0], topo[1] - 0.03, topo[2] - 0.05), 'marrom', escala=(1.2, 1, 0.9))


L.principal(__file__, construir)
