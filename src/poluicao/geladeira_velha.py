"""Geladeira velha tombada no terreno baldio: caixa branca deitada com manchas de ferrugem e a porta entreaberta."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.22, 0.5, 0.2), (0, 0, 0), 'parede', rot=(0, 0, 8))                  # deitada de costas
    L.caixa((0.2, 0.3, 0.025), (0.02, -0.08, 0.2), 'creme', rot=(0, 10, 8))        # porta entreaberta
    L.caixa((0.02, 0.1, 0.02), (0.1, -0.05, 0.22), 'metal', rot=(0, 10, 8))        # puxador
    L.caixa((0.1, 0.12, 0.01), (-0.04, 0.12, 0.2), 'ferrugem', rot=(0, 0, 8))      # ferrugem em cima
    L.caixa((0.012, 0.16, 0.08), (-0.112, 0.06, 0.05), 'ferrugem', rot=(0, 0, 8))  # ferrugem do lado


L.principal(__file__, construir)
