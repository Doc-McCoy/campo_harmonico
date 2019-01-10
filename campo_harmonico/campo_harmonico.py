#!python3
from pychord import Chord

class CampoHarmonico:

	CONSTRUTOR_MAIOR = (0, 2, 2, 1, 2, 2, 2)
	# inicial, tom, tom, semitom, tom, tom, tom
	CARACTERISTICAS = ("", "m", "m", "", "", "m", "m7-5")
	# Maior, menor, menor, maior, maior, menor, diminuta
	# Os campos vazios "" são acordes maiores,
	# Ocultei os 'M' nos acordes maiores pois o pychord não os 
	# reconhece no momento de instanciar.

	def set_scale(self, nota, complemento='M'):
		''' Define em qual escala o campo será baseado. '''
		self.nota = Chord(nota)
		self.complemento = complemento

	def set_field(self):
		''' Monta os acordes do campo harmônico. '''
		note = self.nota
		index_caracteristicas = 0
		self.field = []

		for i in self.CONSTRUTOR_MAIOR:
			note.transpose(i, self.nota.chord)
			self.field.append(note.chord + self.CARACTERISTICAS[index_caracteristicas])
			index_caracteristicas += 1

		return self.field

	def set_notes(self):
		''' Define a lista de notas que a tonalidade pode usar. '''
		notas = []
		for i in self.field:
			nota = Chord(i)
			notas += nota.components()

		notas = list(set(notas))

		return notas

if __name__=='__main__':
	pass

# Ja esta montando o fieid, falta colocar se é maior ou menor.