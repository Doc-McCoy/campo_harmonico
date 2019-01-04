#!python3
from pychord import Chord
from pychord.constants import NOTE_VAL_DICT 

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
