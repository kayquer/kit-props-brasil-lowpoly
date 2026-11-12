"""Lixeiras de coleta seletiva simples: três lixeiras lado a lado (azul, vermelha e verde) numa base de concreto."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.52, 0.2, 0.025), (0, 0, 0), 'concreto')
    for (x, cor, tampa) in ((-0.17, 'cano', 'telhado_azul'), (0, 'vermelho', 'telhado_vermelho'),
                            (0.17, 'verde_garrafa', 'telhado_verde')):
        L.caixa((0.14, 0.14, 0.22), (x, 0, 0.025), cor)
        L.caixa((0.15, 0.15, 0.025), (x, 0, 0.245), tampa)
        L.caixa((0.08, 0.005, 0.04), (x, -0.072, 0.17), 'parede')


L.principal(__file__, construir)
