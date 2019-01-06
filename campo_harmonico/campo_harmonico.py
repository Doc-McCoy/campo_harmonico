#!python3
from pychord import Chord

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

class CampoHarmonico:

	CONSTRUTOR_MAIOR = (2, 2, 1, 2, 2, 2)
	# tom, tom, semitom, tom, tom, tom
	CARACTERÍSTICAS = ("M", "m", "m", "M", "M", "m", "º")
	# Maior, menor, menor, maior, maior, menor, diminuta
	
	def set_scale(self, nota, complemento='M'):
		''' Define em qual escala o campo será baseado. '''
		self.nota = Chord(nota)
		self.complemento = complemento

	def set_field(self):
		''' Monta os acordes do campo harmônico. '''
		note = self.nota
		field = [note.chord]
		count = 1
		for i in self.CONSTRUTOR_MAIOR:
			note.transpose(i)
			field.append(note.chord)
		
		return field

if __name__=='__main__':
	teste = CampoHarmonico()
	teste.set_scale('C')
	field = teste.set_field()
	print(field)

# Ja esta montando o fieid, falta colocar se é maior ou menor.