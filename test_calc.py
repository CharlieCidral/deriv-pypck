import unittest
import sympy as sp
from deriv_calc.calculos import (
    calcular_derivada_raiz_quadrada,
    calcular_derivada_funcao_quadratica,
    calcular_derivada_logaritmo,
    calcular_derivada_seno,
    calcular_derivada_cosseno,
)

class TestCalculos(unittest.TestCase):
    def test_calcular_derivada_raiz_quadrada(self):
        self.assertAlmostEqual(calcular_derivada_raiz_quadrada(4), 0.25)

    def test_calcular_derivada_funcao_quadratica(self):
        self.assertEqual(calcular_derivada_funcao_quadratica(2), 7)

    def test_calcular_derivada_logaritmo(self):
        self.assertAlmostEqual(calcular_derivada_logaritmo(sp.exp(1)), 1/sp.exp(1))

    def test_calcular_derivada_seno(self):
        self.assertAlmostEqual(calcular_derivada_seno(sp.pi/2), 0)

    def test_calcular_derivada_cosseno(self):
        self.assertAlmostEqual(calcular_derivada_cosseno(sp.pi/2), -1)

if __name__ == '__main__':
    unittest.main()
