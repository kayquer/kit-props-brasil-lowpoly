"""Moita de bambu: cinco colmos verdes com nós mais escuros, levemente abertos, e tufos de folhinhas no alto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    colmos = ((0, 0, 0.82, (0, 0, 0)), (0.07, 0.03, 0.72, (0, 7, 0)), (-0.06, 0.04, 0.76, (0, -6, 0)),
              (0.02, -0.06, 0.64, (-7, 0, 0)), (-0.03, 0.08, 0.58, (8, 0, 0)))
    for (x, y, h, rot) in colmos:
        L.cilindro(0.016, h, (x, y, 0), 'cana', lados=4, rot=rot)
    # Nós: anéis escuros nos dois colmos mais altos (faixas curtas um pouco mais grossas)
    for (x, y, h, rot) in colmos[:2]:
        L.cilindro(0.02, 0.015, (x, y, h * 0.5), 'verde_escuro', lados=4, rot=rot)
    for (x, y, z, giro) in ((0.02, 0.0, 0.7, 0), (0.1, 0.03, 0.62, 120), (-0.09, 0.04, 0.64, 240), (0.0, -0.08, 0.52, 60)):
        L.caixa((0.12, 0.01, 0.06), (x, y, z), 'folha', rot=(20, 0, giro))


L.principal(__file__, construir)
