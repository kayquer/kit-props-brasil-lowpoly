"""Ninho de joão-de-barro: casinha redonda de barro no alto de um mourão, com a entrada escura de lado e o passarinho na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.04, 0.42, (0, 0.02, 0), 'madeira', lados=5)
    L.esfera(0.1, (0, 0.02, 0.5), 'tijolo', escala=(1.2, 1, 0.85))
    L.caixa((0.06, 0.02, 0.06), (-0.05, -0.065, 0.47), 'escuro')            # entrada
    L.esfera(0.035, (0.07, -0.07, 0.44), 'capivara', escala=(1, 1.3, 0.9))  # joão-de-barro
    L.cone(0.012, 0.03, (0.07, -0.12, 0.45), 'amarelo', lados=3)


L.principal(__file__, construir)
