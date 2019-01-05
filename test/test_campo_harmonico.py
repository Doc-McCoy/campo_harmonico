#!python3
import unittest
from campo_harmonico.campo_harmonico import CampoHarmonico

class TestHarmonicFields(unittest.TestCase):

    def setUp(self):
        self.classe = CampoHarmonico()
        print('Iniciando testes...')

if __name__ == '__main__':
    unittest.main()
