#!python3
from pychord import Chord

class CampoHarmonico:

	CONSTRUTOR_MAIOR = (0, 2, 2, 1, 2, 2, 2)
	# inicial, tom, tom, semitom, tom, tom, tom
	CARACTERÍSTICAS = ("M", "m", "m", "M", "M", "m", "7-5")
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