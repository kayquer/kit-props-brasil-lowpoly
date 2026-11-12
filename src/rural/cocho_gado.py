"""Cocho de madeira para o gado com água, sobre dois pés, e um bloco de sal mineral branco ao lado."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.18, 0.18):
        L.caixa((0.05, 0.2, 0.06), (x, 0, 0), 'madeira_escura')
    L.tanque(0.5, 0.16, 0.1, (0, 0, 0.06), cor_agua='agua', cor='madeira', parede=0.025, nivel=0.025)
    L.caixa((0.08, 0.08, 0.07), (0.33, -0.08, 0), 'branco', rot=(0, 0, 20))


L.principal(__file__, construir)
