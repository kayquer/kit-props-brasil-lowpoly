"""Monte de lixo: sacos pretos e coloridos, caixas de papelão e latas jogados num terreno."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    for (x, y, r, cor) in ((0, 0, 0.14, 'lixo_preto'), (0.2, 0.06, 0.1, 'lixo_preto'),
                           (-0.17, 0.08, 0.1, 'cano'), (0.05, 0.18, 0.09, 'lixo_preto')):
        L.esfera(r, (x, y, r * 0.8), cor, escala=(1, 1, 0.85))
    L.caixa((0.14, 0.12, 0.1), (-0.12, -0.16, 0), 'cavaco', rot=(0, 0, 25))
    L.caixa((0.1, 0.1, 0.06), (0.06, 0.08, 0.2), 'creme', rot=(10, 0, -15))
    L.cilindro(0.025, 0.07, (0.2, -0.16, 0), 'vermelho', lados=5)
    L.cilindro(0.025, 0.07, (0.3, -0.05, 0.025), 'metal', lados=5, rot=(0, 90, 30))


L.principal(__file__, construir)
