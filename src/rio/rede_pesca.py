"""Rede de pesca verde secando ao sol, pendurada e caída entre duas estacas na beira do rio, com boias laranja."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.32, 0.32):
        L.cilindro(0.018, 0.5, (x, 0, 0), 'madeira_escura', lados=4)
    L.caixa((0.66, 0.01, 0.01), (0, 0, 0.46), 'creme')
    # Rede caída no meio (duas folhas em V) e as linhas da malha
    L.caixa((0.33, 0.008, 0.24), (-0.155, 0, 0.22), 'verde_garrafa', rot=(0, -12, 0))
    L.caixa((0.33, 0.008, 0.24), (0.155, 0, 0.22), 'verde_garrafa', rot=(0, 12, 0))
    for (x, ang) in ((-0.155, -12), (0.155, 12)):
        L.caixa((0.33, 0.014, 0.008), (x, -0.003, 0.34), 'creme', rot=(0, ang, 0))
    for x in (-0.2, 0.0, 0.2):
        L.caixa((0.045, 0.025, 0.035), (x, -0.006, 0.43), 'laranja')


L.principal(__file__, construir)
