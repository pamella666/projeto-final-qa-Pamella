import unittest

# Função a ser testada
def soma(a, b):
    return a + b

# Classe de teste
class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(1, 2), 3)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -2), -3)

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)

# Executar os testes
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
