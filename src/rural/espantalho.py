"""Espantalho: camisa azul numa cruz de madeira, cabeça de palha e chapéu de palha, com palha saindo das mangas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.016, 0.62, (0, 0, 0), 'madeira_escura', lados=4)
    L.caixa((0.42, 0.03, 0.03), (0, 0, 0.44), 'madeira_escura')
    L.caixa((0.14, 0.07, 0.2), (0, 0, 0.3), 'telhado_azul')
    L.caixa((0.34, 0.06, 0.06), (0, 0, 0.42), 'telhado_azul')
    for x in (-0.2, 0.2):
        L.cilindro(0.025, 0.05, (x, 0, 0.43), 'feno', lados=4, r_topo=0, rot=(0, 90 if x > 0 else -90, 0))
    L.esfera(0.055, (0, 0, 0.55), 'feno')
    L.cilindro(0.1, 0.012, (0, 0, 0.59), 'cana_seca', lados=6)
    L.cilindro(0.05, 0.05, (0, 0, 0.6), 'cana_seca', lados=6)


L.principal(__file__, construir)
