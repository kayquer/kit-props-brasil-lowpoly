"""Mesa e duas cadeiras de plástico brancas na calçada, como as de bar de bairro (sem logotipo)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def cadeira(x, y, vira):
    """Cadeira com as laterais cheias (no lugar de 4 pés), assento e encosto; vira = 1 encosto em +Y, -1 em -Y."""
    for dx in (-0.06, 0.06):
        L.caixa((0.012, 0.13, 0.12), (x + dx, y, 0), 'branco')
    L.caixa((0.14, 0.14, 0.015), (x, y, 0.12), 'branco')
    L.caixa((0.14, 0.015, 0.13), (x, y + vira * 0.065, 0.135), 'branco', rot=(vira * -8, 0, 0))


def construir():
    L.cilindro(0.025, 0.2, (0, 0, 0), 'branco', lados=4)
    L.cilindro(0.15, 0.02, (0, 0, 0.2), 'branco', lados=6)
    cadeira(0, 0.24, 1)
    cadeira(0, -0.24, -1)


L.principal(__file__, construir)
