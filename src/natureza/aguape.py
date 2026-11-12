"""Aguapés: tufos de folhas redondas boiando juntos, com espigas de flores lilás (crescem onde a água tem esgoto)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, r, cor) in ((0, 0, 0.09, 'verde'), (0.14, 0.05, 0.075, 'folha'), (-0.12, 0.07, 0.07, 'verde_escuro'),
                           (0.04, -0.13, 0.07, 'folha'), (-0.08, -0.1, 0.06, 'verde')):
        L.esfera(r, (x, y, 0.02), cor, escala=(1, 1, 0.6))
    L.cilindro(0.025, 0.1, (0.0, 0.0, 0.06), 'lilas', lados=5, r_topo=0.012)
    L.cilindro(0.022, 0.08, (0.14, 0.05, 0.05), 'lilas', lados=5, r_topo=0.01)


L.principal(__file__, construir)
