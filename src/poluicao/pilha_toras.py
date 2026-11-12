"""Pilha de toras grossas de mata derrubada, empilhadas na clareira esperando o caminhão, com as pontas cortadas claras."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    r = 0.075
    comp = 0.62
    toras = [(-0.15, r), (0, r), (0.15, r), (-0.075, r * 2.7), (0.075, r * 2.7), (0, r * 4.4)]
    for (y, z) in toras:
        L.cilindro(r, comp, (-comp / 2, y, z), 'madeira_escura', lados=5, rot=(0, 90, 0))
    # Pontas cortadas claras no lado direito (+X, o lado que a câmera vê), só nas de cima
    for (y, z) in toras[3:]:
        L.cilindro(r * 0.85, 0.01, (comp / 2, y, z), 'madeira_clara', lados=5, rot=(0, 90, 0))


L.principal(__file__, construir)
