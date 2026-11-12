"""Barril de captação de chuva: tambor azul num estrado, com o cano da calha descendo, torneira e marcador de nível."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.4, 0.38, 0.06), (0, 0, 0), 'madeira')
    L.cilindro(0.15, 0.36, (0, 0, 0.06), 'cano', lados=8)
    L.cilindro(0.155, 0.025, (0, 0, 0.42), 'agua_funda', lados=8)
    L.cano((0.03, 0.05, 0.44), (0.03, 0.05, 0.82), 0.028, 'metal', lados=4)
    L.cano((0.03, 0.05, 0.82), (0.03, 0.2, 0.92), 0.028, 'metal', lados=4)
    L.cano((0, -0.14, 0.14), (0, -0.21, 0.14), 0.015, 'metal_escuro', lados=3)
    L.caixa((0.012, 0.03, 0.26), (0.155, 0, 0.12), 'parede')
    L.caixa((0.014, 0.032, 0.15), (0.156, 0, 0.12), 'agua')


L.principal(__file__, construir)
