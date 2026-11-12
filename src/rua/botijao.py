"""Botijão de gás cinza de cozinha, com base, ombro arredondado, válvula e a alça de proteção no alto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.1, 0.03, (0, 0, 0), 'metal_escuro', lados=8)                  # base
    L.cilindro(0.11, 0.16, (0, 0, 0.03), 'concreto_escuro', lados=8)            # corpo
    L.cilindro(0.11, 0.05, (0, 0, 0.19), 'concreto_escuro', lados=8, r_topo=0.05)  # ombro
    L.cilindro(0.02, 0.04, (0, 0, 0.24), 'metal', lados=4)                       # válvula
    for x in (-0.05, 0.05):
        L.caixa((0.015, 0.06, 0.07), (x, 0, 0.22), 'metal_escuro')               # alça


L.principal(__file__, construir)
