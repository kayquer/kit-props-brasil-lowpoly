"""Cavalete de calçada em A, de madeira, com um quadro-negro que só mostra o desenho de um prato (sem letras)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.26, 0.02, 0.42), (0, -0.06, 0), 'madeira', rot=(-12, 0, 0))   # folha da frente
    L.caixa((0.26, 0.02, 0.42), (0, 0.06, 0), 'madeira', rot=(12, 0, 0))     # folha de trás
    L.caixa((0.21, 0.01, 0.3), (0, -0.063, 0.07), 'escuro', rot=(-12, 0, 0)) # quadro-negro
    # A folha da frente inclina para trás: na altura z a face dela fica em y ≈ -0.07 + 0.21·z
    L.cilindro(0.06, 0.008, (0, -0.04, 0.24), 'branco', lados=8, rot=(78, 0, 0))   # prato
    L.cilindro(0.03, 0.009, (0, -0.047, 0.24), 'laranja', lados=6, rot=(78, 0, 0))  # comida


L.principal(__file__, construir)
