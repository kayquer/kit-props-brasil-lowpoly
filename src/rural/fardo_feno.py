"""Fardo de feno redondo: rolo de palha deitado no pasto, com as faces das pontas mais escuras."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lib as L  # noqa: E402


def construir():
    L.cilindro(0.17, 0.28, (-0.14, 0, 0.17), 'feno', lados=8, rot=(0, 90, 0))
    L.cilindro(0.13, 0.01, (-0.145, 0, 0.17), 'cana_seca', lados=8, rot=(0, 90, 0))
    L.cilindro(0.13, 0.01, (0.135, 0, 0.17), 'cana_seca', lados=8, rot=(0, 90, 0))


L.principal(__file__, construir)
