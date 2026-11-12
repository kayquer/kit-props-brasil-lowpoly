"""Pescaria na margem: vara de bambu fincada no barranco com a linha e a boia na água à frente, puçá e balde ao lado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.14, (0, 0.12, 0.0), 'terra', escala=(1.3, 1, 0.45))               # barranco
    L.cano((0, 0.12, 0.04), (0, -0.42, 0.5), 0.012, 'cana', lados=4)             # vara inclinada para a água
    L.cano((0, -0.42, 0.5), (0, -0.46, 0.02), 0.003, 'branco', lados=3)          # linha
    L.esfera(0.022, (0, -0.46, 0.01), 'vermelho')                                 # boia
    L.cano((0.17, 0.12, 0.0), (0.2, 0.0, 0.26), 0.008, 'madeira', lados=4)       # cabo do puçá
    L.cone(0.07, 0.1, (0.21, -0.02, 0.2), 'pedra', lados=6)                       # rede do puçá
    L.cilindro(0.05, 0.08, (-0.16, 0.08, 0), 'cano', lados=5, r_topo=0.06)        # balde de minhoca


L.principal(__file__, construir)
