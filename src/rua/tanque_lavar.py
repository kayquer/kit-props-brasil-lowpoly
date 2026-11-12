"""Tanque de lavar roupa de cimento: cuba com água e esfregador, sobre um pé, com torneira e uma barra de sabão azul."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.12, 0.14, 0.2), (0, 0.02, 0), 'concreto_escuro')               # pé
    L.caixa((0.36, 0.26, 0.1), (0, 0, 0.2), 'concreto')                        # cuba
    L.caixa((0.15, 0.2, 0.012), (-0.08, 0.0, 0.295), 'agua')                    # água
    L.caixa((0.14, 0.2, 0.02), (0.1, 0.0, 0.29), 'concreto_escuro', rot=(0, -12, 0))  # esfregador
    L.cano((-0.08, 0.13, 0.3), (-0.08, 0.13, 0.42), 0.01, 'metal', lados=4)    # cano
    L.cano((-0.08, 0.13, 0.42), (-0.08, 0.06, 0.4), 0.01, 'metal', lados=4)    # torneira
    L.caixa((0.06, 0.035, 0.025), (0.12, -0.06, 0.31), 'cano')                  # sabão azul


L.principal(__file__, construir)
