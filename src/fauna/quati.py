"""Quati: bicho marrom de focinho comprido e arrebitado, com a cauda listrada levantada bem alto atrás."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.1, 0.035, 0.07), (0, -0.08, 0), 'madeira_escura')    # patas da frente
    L.caixa((0.1, 0.035, 0.07), (0, 0.1, 0), 'madeira_escura')      # patas de trás
    L.esfera(0.1, (0, 0.01, 0.13), 'capivara', escala=(0.75, 1.45, 0.7))
    L.esfera(0.05, (0, -0.15, 0.15), 'capivara', escala=(0.9, 1, 0.9))
    L.cilindro(0.025, 0.1, (0, -0.18, 0.15), 'madeira_escura', lados=4, r_topo=0.01, rot=(80, 0, 0))  # focinho
    # Cauda listrada: trechos alternados subindo e curvando para a frente
    trechos = [(0, 0.15, 0.13), (0, 0.2, 0.24), (0, 0.21, 0.35), (0, 0.18, 0.45)]
    for i, (a, b) in enumerate(zip(trechos, trechos[1:])):
        L.cano(a, b, 0.028, 'creme' if i % 2 else 'madeira_escura', lados=4)


L.principal(__file__, construir)
