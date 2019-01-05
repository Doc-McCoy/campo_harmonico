#!python3
from pychord import Chord
from pychord.constants import NOTE_VAL_DICT, SHARPED_SCALE

'''
Campo harmonico maior:
C | D | E | F | G | A | B
1 | 2 | 3 | 4 | 5 | 6 | 7

3 tipos de acorde:
- Maior
- Menor
- Diminuto

Fórmula do campo harmônio maior:
1T | 1T | 1/2T | 1T | 1T | 1T | 1/2T

Sequencia:
IM | IIm | IIIm | IVM | VM | VIm | VIIº

'''

class HarmonicFields:

	notas_validas = NOTE_VAL_DICT.keys()
	
	def set_scale(self, note, complement='M'):
		''' Define em qual escala o campo será baseado. '''
		if note in self.notas_validas and complement in ('m', 'M'):
			self.scale = note+complement
		else:
			print("Nota ou complemento inexistente")

if __name__=='__main__':
	teste = HarmonicFields()
	teste.set_scale('A#')
