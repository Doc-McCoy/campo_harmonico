#!python3
import unittest
from pychord import Chord
from campo_harmonico.campo_harmonico import CampoHarmonico

class TestHarmonicFields(unittest.TestCase):

    def setUp(self):
        self.app = CampoHarmonico()

    def test_set_scale(self):
        self.app.set_scale("C")
        self.assertIsInstance(self.app.nota, Chord)
        self.assertEqual(self.app.nota, Chord("C"))

    def test_set_field(self):
        escala_c = ["C", "Dm", "Em", "F", "G", "Am", "Bm7-5"]
        escala_d = ["D", "Em", "F#m", "G", "A", "Bm", "C#m7-5"]
        escala_e = ["E", "F#m", "G#m", "A", "B", "C#m", "D#m7-5"]
        escala_f = ["F", "Gm", "Am", "Bb", "C", "Dm", "Em7-5"]
        escala_g = ["G", "Am", "Bm", "C", "D", "Em", "F#m7-5"]
        escala_a = ["A", "Bm", "C#m", "D", "E", "F#m", "G#m7-5"]
        escala_b = ["B", "C#m", "D#m", "E", "F#", "G#m", "A#m7-5"]

        self.app.set_scale("C")
        field = self.app.set_field()
        self.assertEqual(field, escala_c)

        self.app.set_scale("D")
        field = self.app.set_field()
        self.assertEqual(field, escala_d)
        
        self.app.set_scale("E")
        field = self.app.set_field()
        self.assertEqual(field, escala_e)

        self.app.set_scale("F")
        field = self.app.set_field()
        self.assertEqual(field, escala_f)

        self.app.set_scale("G")
        field = self.app.set_field()
        self.assertEqual(field, escala_g)

        self.app.set_scale("A")
        field = self.app.set_field()
        self.assertEqual(field, escala_a)

        self.app.set_scale("B")
        field = self.app.set_field()
        self.assertEqual(field, escala_b)
    

if __name__ == '__main__':
    unittest.main()
