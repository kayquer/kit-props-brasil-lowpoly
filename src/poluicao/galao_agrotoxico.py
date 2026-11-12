"""Galões de agrotóxico vazios jogados no chão (sem rótulo), um tombado, com uma mancha escura de vazamento."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.2, (0.02, 0.0, 0.0), 'chorume', escala=(1.2, 1, 0.06))                   # mancha
    L.caixa((0.12, 0.08, 0.16), (-0.1, 0.06, 0), 'branco')                               # galão em pé
    L.cilindro(0.022, 0.03, (-0.12, 0.06, 0.16), 'escuro', lados=4)
    L.caixa((0.02, 0.06, 0.04), (-0.065, 0.06, 0.15), 'branco')                          # alça
    L.caixa((0.11, 0.07, 0.14), (0.1, 0.07, 0), 'amarelo')                               # galão em pé
    L.cilindro(0.02, 0.03, (0.1, 0.07, 0.14), 'escuro', lados=4)
    L.caixa((0.16, 0.12, 0.08), (0.04, -0.12, 0), 'branco', rot=(0, 0, 25))              # galão tombado
    L.cilindro(0.02, 0.04, (0.09, -0.15, 0.04), 'escuro', lados=4, rot=(0, 90, 25))


L.principal(__file__, construir)
