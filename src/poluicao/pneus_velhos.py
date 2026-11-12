"""Pneus velhos: dois pneus empilhados com água parada dentro e um terceiro largado ao lado (criadouro do mosquito)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.anel(0.14, 0.07, 0.07, (0, 0, 0), 'escuro', lados=5)
    L.anel(0.14, 0.07, 0.07, (0.01, 0.01, 0.07), 'lixo_preto', lados=5)
    L.cilindro(0.075, 0.11, (0.01, 0.01, 0.0), 'agua_suja', lados=5)
    L.anel(0.13, 0.065, 0.065, (0.28, -0.08, 0), 'escuro', lados=5)


L.principal(__file__, construir)
