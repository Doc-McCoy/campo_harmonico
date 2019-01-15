#!python3
import unittest
from pychord import Chord
from campo_harmonico.campo_harmonico import CampoHarmonico

class TestHarmonicFields(unittest.TestCase):

    def setUp(self):
        """ Instanciar a classe que será testada. """
        self.app = CampoHarmonico()

    def test_set_scale(self):
        """ Seta um tom para a classe. """
        self.app.set_scale("C")
        self.assertIsInstance(self.app.nota, Chord)
        self.assertEqual(self.app.nota, Chord("C"))

    def test_set_field(self):
        """ Testa o construtor de campo harmônico para todos os tons. """
        escala_c_major = ["C", "Dm", "Em", "F", "G", "Am", "Bm7-5"]
        escala_d_major = ["D", "Em", "F#m", "G", "A", "Bm", "C#m7-5"]
        escala_e_major = ["E", "F#m", "G#m", "A", "B", "C#m", "D#m7-5"]
        escala_f_major = ["F", "Gm", "Am", "A#", "C", "Dm", "Em7-5"]
        escala_g_major = ["G", "Am", "Bm", "C", "D", "Em", "F#m7-5"]
        escala_a_major = ["A", "Bm", "C#m", "D", "E", "F#m", "G#m7-5"]
        escala_b_major = ["B", "C#m", "D#m", "E", "F#", "G#m", "A#m7-5"]

        self.app.set_scale("C")
        field = self.app.set_field()
        self.assertEqual(field, escala_c_major)

        self.app.set_scale("D")
        field = self.app.set_field()
        self.assertEqual(field, escala_d_major)

        self.app.set_scale("E")
        field = self.app.set_field()
        self.assertEqual(field, escala_e_major)

        self.app.set_scale("F")
        field = self.app.set_field()
        self.assertEqual(field, escala_f_major)

        self.app.set_scale("G")
        field = self.app.set_field()
        self.assertEqual(field, escala_g_major)

        self.app.set_scale("A")
        field = self.app.set_field()
        self.assertEqual(field, escala_a_major)

        self.app.set_scale("B")
        field = self.app.set_field()
        self.assertEqual(field, escala_b_major)

    def test_set_notes(self):
        """ Testa a lista de notas que o tom poderá usar. """
        self.app.set_scale("C")
        self.app.set_field()
        notes = self.app.set_notes()
        self.assertTrue(set(notes).issubset(["C", "D", "E", "F", "G", "A", "B"]))


if __name__ == '__main__':
    unittest.main()
