"""Mandacaru: cacto do sertão com o tronco reto e dois braços subindo, para encostas secas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.065, 0.62, (0, 0, 0), 'cacto', lados=5, r_topo=0.05)
    L.cilindro(0.04, 0.16, (0.04, 0, 0.26), 'cacto', lados=5, rot=(0, 90, 0))
    L.cilindro(0.04, 0.22, (0.17, 0, 0.26), 'cacto', lados=5, r_topo=0.03)
    L.cilindro(0.035, 0.13, (-0.04, 0, 0.36), 'cacto', lados=5, rot=(0, -90, 0))
    L.cilindro(0.035, 0.16, (-0.15, 0, 0.36), 'cacto', lados=5, r_topo=0.025)
    L.cone(0.05, 0.05, (0.1, -0.12, 0), 'terra', lados=5)


L.principal(__file__, construir)
