#!python3

'''
Programa pica que eu nunca termino que monta toda uma escala a partir do tom que você
deseja compor uma música.
'''

notas = ['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#',
		'La','La#','Si','Do','Do#','Re','Re#','Mi','Fa','Fa#',
		'Sol','Sol#','La','La#','Si']
"""
notasMenores = ['Do','Reb','Re','Mib','Mi','Fa','Solb','Sol',
			'Lab','La','Sib','Si','Do','Reb','Re','Mib','Mi',
			'Fa','Solb','Sol','Lab','La','Sib','Si']
"""
acordes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B',
		'C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

acordesBemois = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B',
			'C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

construtorMaior = [0, 2, 4, 5, 7, 9, 11, 12] # tom, tom, semitom, tom, tom, tom, semitom
construtorMenor = [0, 2, 3, 5, 7, 8, 10, 12] # tom, semitom, tom, tom, semitom, tom, tom

escala = []
escalaAcordes = []
relativas = []
pentatonicas = []
index = int()

'''
dicRelativas = {'C':'Am',
			'G':'Em',
			'D':'Bm',
			'A':'F#m',
			'E':'C#m',
			'B':'G#m',
			'F#':'D#m',
			'C#':'A#m',
			'F':'Dm',
			'Bb':'Gm',
			'Eb':'Cm',
			'Ab':'Fm',
			'Db':'Bbm',
			'Gb':'Ebm',
			'Cb':'Abm'}
			# da maior pra menor: 6 grau
			# da menor pra maior: 1 tom e meio!

relativasInv = dict((v, k) for (k, v) in relativas.items())

'''
# Notas -----------------------------------------------------------------------
def setNotas(constr, index):
	'''Monta a lista de notas que podem ser utilizadas'''
	for i in constr:
		escala.append(notas[index+i])

# Campo Harmonico -------------------------------------------------------------
def setCampo(constr, index):
	'''Monta a lista de acordes que podem ser utilizados'''
	grau = 0
	for i in constr:
		escalaAcordes.append(acordes[index+i])
		if (grau==1 or grau==2 or grau==5 or grau==6):
			escalaAcordes[grau] += 'm'
			if (grau==6):
				escalaAcordes[grau] += '(b5)'
		grau += 1

# Relativas -------------------------------------------------------------------
def setRelativas(escalaAcordes):
	'''Monta o campo de relativas'''
	for i in escalaAcordes:
		if 'm' in i:
			i = i.replace('m','') # tirar o 'm'
			if ('#' in i or 'b' in i): # verfiicar se tem # ou b
				index = acordes.index(i[0:2])
				relativas.append(index+3)
			else:
				index = acordes.index(i)
				relativas.append(index+3)
		else:
			index = acordes.index(i)
			relativas.append(acordes[index-3]+'m')
			# Isso vai dar erro, pois o 'm' sera inserido sempre no
			# final. Arrumar.

def setPentatonicas(index, modo):
	'''Define as notas pentatonicas'''
	if modo == "M":
		for i in (0, 2, 4, 7, 9):
			pentatonicas.append(notas[index+i])
	elif modo == "m":
		for i in (0, 3, 5, 7, 10):
			pentatonicas.append(notas[index+i])

# Main ------------------------------------------------------------------------
def main():
	
	inEscala = input("\nDigite a escala em que deseja compor: ").capitalize()
	modo = input("Digite 'M' para maior ou 'm' para menor: ")

	# Localizar Index ---------------------------------------------------------
	if inEscala in acordes:
		index = acordes.index(inEscala)
	elif inEscala in acordesBemois:
		index = acordesBemois.index(inEscala)
	else:
		print("Escala inexistente.")
		exit()

	# Construcao --------------------------------------------------------------
	if modo == 'M':
		setNotas(construtorMaior, index)
		setCampo(construtorMaior, index)

	elif modo == 'm':
		setNotas(construtorMenor, index)
		setCampo(construtorMenor, index)

	else:
		print("Erro!")

	setPentatonicas(index, modo)
	#setRelativas(escalaAcordes)

	# Escala ----------------------------------------------------------------------
	print("\n\nNotas a serem utilizadas:")
	print("------------------------------------------")
	print("| %s | %s | %s | %s | %s | %s | %s |" % (escala[0], escala[1], escala[2], escala[3], escala[4], escala[5], escala[6]))
	print("------------------------------------------")

	# Campo Harmonico -------------------------------------------------------------
	print("\nAcordes a serem utilizados:")
	print("------------------------------------------")
	print("| %s | %s | %s | %s | %s | %s | %s |" % (escalaAcordes[0], escalaAcordes[1], escalaAcordes[2], escalaAcordes[3], escalaAcordes[4], escalaAcordes[5], escalaAcordes[6]))
	print("------------------------------------------")

	# Relativas -------------------------------------------------------------------
	# Detectar o m no final para saber quantos graus avancar / retroceder
	print("\nRelativas:")
	print("------------------------------------------")
	#print "| %s | %s | %s | %s | %s | %s | %s |" % (relativas[0], relativas[1], relativas[2], relativas[3], relativas[4], relativas[5], relativas[6])
	print("------------------------------------------")
	
	# Pentatonicas ----------------------------------------------------------------
	'''
	Maior: Tonica - 2 maior - 3 maior - 5 justa - 6 maior (0, 2, 4, 7, 9)
	Menor: Tonica, 3 menor - 4 justa - 5 justa - 7 menor (0, 3, 5, 7, 10)
	'''
	print("\nPentatonicas:")
	print("----------------------------")
	print("| %s | %s | %s | %s | %s |" % (pentatonicas[0], pentatonicas[1], pentatonicas[2], pentatonicas[3], pentatonicas[4]))
	print("----------------------------")

	# Harmonia Funcional ----------------------------------------------------------
	print("\nHarmonia Funcional:")
	print("------------------------------------------")
	print("Tonicas: %s, %s, %s" % (escalaAcordes[0], escalaAcordes[2], escalaAcordes[5]))
	print("Dominantes: %s, %s" % (escalaAcordes[4], escalaAcordes[6]))
	print("Subdominantes: %s, %s" % (escalaAcordes[1], escalaAcordes[3]))
	print("------------------------------------------")

# TODO: GUI -------------------------------------------------------------------

if __name__=='__main__':
	main()
