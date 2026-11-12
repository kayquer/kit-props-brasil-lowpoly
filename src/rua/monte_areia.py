"""Monte de areia de obra na calçada, com uma pá fincada no alto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cone(0.26, 0.17, (0, 0, 0), 'areia', lados=8)
    L.cone(0.15, 0.1, (0.17, -0.1, 0), 'areia', lados=6)
    L.cano((0.02, 0.02, 0.1), (0.07, 0.06, 0.38), 0.011, 'madeira', lados=4)   # cabo da pá
    L.caixa((0.08, 0.012, 0.09), (0.015, 0.015, 0.05), 'metal_escuro', rot=(10, -10, 0))  # lâmina


L.principal(__file__, construir)
