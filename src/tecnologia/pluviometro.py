"""Pluviômetro: funil e tubo medidor de chuva preso num poste de madeira, com a escala de água na frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.12, 0.12, 0.04), (0, 0.04, 0), 'concreto')
    L.caixa((0.045, 0.045, 0.62), (0, 0.04, 0.04), 'madeira_escura')
    L.caixa((0.06, 0.05, 0.03), (0, -0.005, 0.5), 'metal_escuro')
    L.cilindro(0.04, 0.17, (0, -0.06, 0.42), 'parede', lados=6)
    L.cilindro(0.04, 0.06, (0, -0.06, 0.59), 'metal', lados=6, r_topo=0.07)
    L.caixa((0.02, 0.012, 0.1), (0, -0.1, 0.44), 'agua')


L.principal(__file__, construir)
