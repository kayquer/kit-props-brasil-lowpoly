"""Barraca de feira: toldo listrado vermelho e branco sobre quatro varas e uma bancada com caixotes de frutas."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y) in ((-0.3, -0.16), (0.3, -0.16), (-0.3, 0.16), (0.3, 0.16)):
        L.cano((x, y, 0), (x, y, 0.62), 0.01, 'metal', lados=3)
    perfil = ((-0.22, 0.0), (0.22, 0.0), (0.0, 0.12))
    for i, cor in enumerate(('vermelho', 'branco', 'vermelho')):
        L.prisma(perfil, 0.24, (-0.24 + i * 0.24, 0, 0.6), cor, eixo='X')
    L.caixa((0.62, 0.32, 0.03), (0, 0, 0.3), 'madeira')
    for (x, cor) in ((-0.18, 'laranja'), (0.0, 'vermelho'), (0.18, 'amarelo')):
        L.caixa((0.15, 0.13, 0.06), (x, -0.04, 0.33), 'cavaco')
        L.caixa((0.13, 0.11, 0.03), (x, -0.04, 0.38), cor)


L.principal(__file__, construir)
