"""Garça branca: ave pernalta em pé na beira d'água, pescoço em curva e bico amarelo apontando para a frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cano((-0.03, 0.02, 0), (-0.02, 0.02, 0.24), 0.008, 'amarelo', lados=3)
    L.cano((0.03, 0.02, 0), (0.02, 0.02, 0.24), 0.008, 'amarelo', lados=3)
    L.esfera(0.08, (0, 0.03, 0.3), 'branco', escala=(0.75, 1.35, 0.7))
    L.cone(0.04, 0.12, (0, 0.13, 0.31), 'branco', lados=4)
    L.cano((0, -0.04, 0.33), (0, -0.07, 0.47), 0.018, 'branco', lados=4)
    L.esfera(0.035, (0, -0.08, 0.49), 'branco')
    L.cilindro(0.012, 0.09, (0, -0.1, 0.49), 'amarelo', lados=4, r_topo=0, rot=(90, 0, 0))


L.principal(__file__, construir)
