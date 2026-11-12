"""Cano de PVC improvisado saindo do barranco e despejando um fio de esgoto escuro para a frente, na água.

A boca do cano olha para a frente (-Y): o jogo vira a frente para a água."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.esfera(0.17, (0, 0.12, 0.06), 'terra', escala=(1.3, 1, 0.75))                       # barranco
    L.cilindro(0.04, 0.32, (0.03, 0.16, 0.16), 'pvc', lados=6, rot=(96, 0, 0))             # cano
    L.cilindro(0.03, 0.006, (0.03, -0.158, 0.13), 'escuro', lados=6, rot=(96, 0, 0))       # boca
    L.caixa((0.03, 0.012, 0.13), (0.03, -0.18, 0.0), 'esgoto', rot=(-10, 0, 0))            # fio caindo
    L.esfera(0.12, (0.03, -0.24, 0.0), 'esgoto', escala=(1.3, 1, 0.1))                     # mancha na água


L.principal(__file__, construir)
