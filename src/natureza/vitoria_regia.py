"""Vitória-régia: folhas redondas de borda levantada boiando na água, com uma flor rosa no meio."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def folha(x, y, r, borda=True):
    """Folha na superfície (z = 0): a borda é um disco mais escuro um pouco mais alto que o miolo."""
    if borda:
        L.cilindro(r, 0.035, (x, y, -0.01), 'verde_escuro', lados=8)
        L.cilindro(r * 0.9, 0.03, (x, y, -0.002), 'folha', lados=8)
    else:
        L.cilindro(r, 0.02, (x, y, -0.01), 'verde', lados=8)


def construir():
    folha(0, 0, 0.17)
    folha(0.27, 0.1, 0.13)
    folha(-0.2, 0.18, 0.1, borda=False)
    L.cone(0.04, 0.06, (0.27, 0.1, 0.02), 'rosa', lados=5)


L.principal(__file__, construir)
