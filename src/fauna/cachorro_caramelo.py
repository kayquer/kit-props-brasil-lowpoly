"""Cachorro caramelo: vira-lata deitado tomando sol, de orelhas caídas e peito claro, olhando para a frente."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.caixa((0.15, 0.3, 0.09), (0, 0.04, 0), 'caramelo')
    L.caixa((0.11, 0.06, 0.07), (0, -0.12, 0.0), 'creme')
    L.caixa((0.12, 0.11, 0.1), (0, -0.16, 0.06), 'caramelo')
    L.caixa((0.07, 0.06, 0.05), (0, -0.24, 0.07), 'creme')
    for x in (-0.065, 0.065):
        L.caixa((0.025, 0.05, 0.07), (x, -0.15, 0.08), 'madeira')
        L.caixa((0.035, 0.08, 0.025), (x * 0.7, -0.22, 0), 'creme')
    L.cano((0.03, 0.18, 0.06), (0.11, 0.26, 0.03), 0.015, 'caramelo', lados=4)


L.principal(__file__, construir)
