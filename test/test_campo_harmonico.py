#!python3
import unittest
from pychord import Chord
from campo_harmonico.campo_harmonico import CampoHarmonico

class TestHarmonicFields(unittest.TestCase):

    def setUp(self):
        self.app = CampoHarmonico()
        print('Iniciando testes...')

    def test_set_scale(self):
        self.app.set_scale("C")
        self.assertIsInstance(self.app.nota, Chord)
        self.assertEqual(self.app.nota, Chord("C"))

    def test_set_field(self):
        self.app.set_scale("C")
        field = self.app.set_field()
        self.assertEqual(field, ["C", "Dm", "Em", "F", "G", "Am", "Bmº"])
    

if __name__ == '__main__':
    unittest.main()
