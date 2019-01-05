#!python3
from pychord import Chord
from pychord.constants import NOTE_VAL_DICT

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

	MAJOR_CONSTRUCTOR = (2, 2, 1, 2, 2, 2)
	notas_validas = NOTE_VAL_DICT.keys()
	
	def set_scale(self, note, complement='M'):
		''' Define em qual escala o campo será baseado. '''
		if note in self.notas_validas and complement in ('m', 'M'):
			self.note = Chord(note)
			self.complement = complement
		else:
			print("Nota ou complemento inexistente")

	def form_field(self):
		''' Monta os acordes do campo harmônico. '''
		note = self.note
		field = [note.chord]
		count = 1
		for i in self.MAJOR_CONSTRUCTOR:
			note.transpose(i)
			field.append(note.chord)
		return field

if __name__=='__main__':
	teste = HarmonicFields()
	teste.set_scale('C')
	field = teste.form_field()
	print(field)

# Ja esta montando o fieid, falta colocar se é maior ou menor.