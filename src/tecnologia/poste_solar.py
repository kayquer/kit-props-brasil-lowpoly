"""Poste solar: mastro com placa solar inclinada no topo, bateria no meio e braço com luminária de LED."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.1, 0.07, (0, 0, 0), 'concreto', lados=6, r_topo=0.085)
    L.cilindro(0.032, 1.5, (0, 0, 0.07), 'metal', lados=6, r_topo=0.022)
    L.caixa((0.1, 0.07, 0.16), (0, -0.045, 0.55), 'metal_escuro')
    L.caixa((0.42, 0.3, 0.025), (0, 0, 1.6), 'metal', rot=(-28, 0, 0))
    L.caixa((0.39, 0.27, 0.01), (0, -0.007, 1.623), 'painel_solar', rot=(-28, 0, 0))
    L.cano((0, 0, 1.42), (0.34, 0, 1.49), 0.016, 'metal', lados=4)
    L.caixa((0.18, 0.08, 0.035), (0.38, 0, 1.46), 'metal_escuro')
    L.caixa((0.15, 0.06, 0.01), (0.38, 0, 1.453), 'flor_amarela')


L.principal(__file__, construir)
