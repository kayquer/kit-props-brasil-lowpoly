"""Varal de quintal: arame esticado entre duas forquilhas de bambu, com três roupas coloridas penduradas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for x in (-0.4, 0.4):
        L.cano((x, 0, 0), (x, 0, 0.5), 0.014, 'cana_seca', lados=4)                 # forquilha
        L.cano((x, 0, 0.44), (x + (0.05 if x < 0 else -0.05), 0, 0.56), 0.01, 'cana_seca', lados=3)
    L.cano((-0.4, 0, 0.5), (0.4, 0, 0.5), 0.004, 'metal_escuro', lados=3)           # arame
    for (x, larg, alt, cor) in ((-0.22, 0.16, 0.2, 'vermelho'), (0.0, 0.14, 0.14, 'telhado_azul'), (0.2, 0.17, 0.22, 'amarelo')):
        L.caixa((larg, 0.012, alt), (x, 0, 0.5 - alt), cor)


L.principal(__file__, construir)
