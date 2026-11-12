"""Toco recém-serrado: corte claro e liso no topo, serragem amontoada em volta e lascas de madeira no chão (desmatamento)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.13, 0.16, (0, 0, 0), 'madeira_escura', lados=7, r_topo=0.11)
    L.cilindro(0.105, 0.012, (0, 0, 0.16), 'serragem', lados=7)                     # corte claro
    L.cone(0.2, 0.04, (0.02, -0.04, 0), 'serragem', lados=6)                         # serragem
    L.cone(0.1, 0.03, (-0.18, 0.06, 0), 'serragem', lados=5)
    for (x, y, giro) in ((0.2, -0.12, 30), (-0.14, -0.16, -50), (0.16, 0.14, 80)):
        L.caixa((0.1, 0.03, 0.015), (x, y, 0), 'madeira_clara', rot=(0, 0, giro))   # lascas


L.principal(__file__, construir)
