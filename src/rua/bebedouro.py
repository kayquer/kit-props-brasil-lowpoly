"""Bebedouro público: pedestal de concreto, cuba turquesa com bica de metal e uma tigela de água para os animais."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.15, 0.03, (0, 0, 0), 'concreto', lados=6)
    L.cilindro(0.075, 0.3, (0, 0, 0.03), 'concreto', lados=6, r_topo=0.055)
    L.cilindro(0.12, 0.05, (0, 0, 0.33), 'agua_funda', lados=6, r_topo=0.14)
    L.cilindro(0.115, 0.012, (0, 0, 0.372), 'agua', lados=6)
    L.cano((0, 0.03, 0.37), (0, -0.03, 0.43), 0.012, 'metal', lados=3)
    L.cilindro(0.06, 0.03, (0.17, -0.12, 0), 'metal', lados=6)
    L.cilindro(0.048, 0.032, (0.17, -0.12, 0), 'agua', lados=6)


L.principal(__file__, construir)
