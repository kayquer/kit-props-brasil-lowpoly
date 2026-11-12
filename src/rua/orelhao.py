"""Orelhão: cabine telefônica em forma de concha laranja num pé de metal, aberta para a frente (sem marca)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.08, 0.02, (0, 0.04, 0), 'concreto', lados=6)
    L.cilindro(0.022, 0.5, (0, 0.06, 0.02), 'metal_escuro', lados=4)
    L.esfera(0.18, (0, 0.05, 0.66), 'laranja', escala=(1, 0.85, 1.2))
    # A abertura: um oval escuro rente à frente da concha, com o telefone dentro
    L.esfera(0.14, (0, -0.07, 0.63), 'escuro', escala=(0.85, 0.35, 1.0))
    L.caixa((0.06, 0.03, 0.09), (0, -0.115, 0.6), 'metal')


L.principal(__file__, construir)
