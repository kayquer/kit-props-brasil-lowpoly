"""Caixa d'água de polietileno: tanque azul de tampa cônica numa base baixa de concreto, de quintal ou laje."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.4, 0.4, 0.08), (0, 0, 0), 'concreto')
    L.cilindro(0.16, 0.22, (0, 0, 0.08), 'cano', lados=8, r_topo=0.185)
    L.cilindro(0.195, 0.05, (0, 0, 0.3), 'telhado_azul', lados=8, r_topo=0.12)
    L.cano((0.17, 0, 0.12), (0.26, 0, 0.12), 0.015, 'parede', lados=4)


L.principal(__file__, construir)
