"""Placa de rua: placa azul com faixa branca (sem letras) no alto de um poste fino de metal."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.016, 0.9, (0, 0, 0), 'metal', lados=4)
    L.caixa((0.34, 0.02, 0.11), (0, -0.02, 0.8), 'telhado_azul')
    L.caixa((0.26, 0.006, 0.022), (0, -0.032, 0.844), 'parede')


L.principal(__file__, construir)
