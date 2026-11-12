"""Bananeira: touceira de tronco curto e grosso com folhas largas abertas em leque e um cacho de banana verde."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.055, 0.32, (0, 0, 0), 'verde_escuro', lados=5, r_topo=0.04)
    L.cilindro(0.035, 0.16, (0.09, 0.05, 0), 'verde', lados=5, r_topo=0.025)   # filhote da touceira
    # Folhas largas (caixas finas) saindo do topo, inclinadas para fora em leque
    for (giro, incl, cor) in ((0, 55, 'banana'), (72, 60, 'verde'), (144, 50, 'banana'), (216, 62, 'verde'), (288, 52, 'banana')):
        L.caixa((0.11, 0.012, 0.34), (0, 0, 0.28), cor, rot=(incl, 0, giro))
    L.esfera(0.05, (0.0, -0.06, 0.24), 'cana', escala=(0.9, 0.9, 1.3))  # cacho


L.principal(__file__, construir)
