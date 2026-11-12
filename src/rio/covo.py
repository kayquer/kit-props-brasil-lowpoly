"""Covo de pesca: armadilha cilíndrica de tala trançada deitada na beira, com a boca de funil virada para a água (frente)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    # Corpo deitado ao longo de Y, meio afundado (o jogo põe na margem com a frente -Y para a água)
    L.cilindro(0.09, 0.4, (0, 0.2, 0.06), 'cana_seca', lados=6, rot=(90, 0, 0))
    for y in (0.08, -0.06):
        L.cilindro(0.095, 0.02, (0, y, 0.06), 'madeira', lados=6, rot=(90, 0, 0))      # aros
    L.cilindro(0.09, 0.08, (0, -0.2, 0.06), 'madeira', lados=6, r_topo=0.03, rot=(-90, 0, 0))  # boca (funil)
    L.cano((0.11, 0.24, 0), (0.11, 0.24, 0.26), 0.012, 'madeira_escura', lados=4)    # estaca
    L.cano((0.11, 0.24, 0.2), (0.03, 0.2, 0.1), 0.004, 'cana_seca', lados=3)        # amarra


L.principal(__file__, construir)
