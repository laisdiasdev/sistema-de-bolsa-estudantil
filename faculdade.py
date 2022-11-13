class Facul:
	def __init__(self, nome, cursos):
		self.cursos = cursos
		self.nome = nome
	pass

	def mostrarCursos(self):
		print(f"\nCursos disponíveis para a faculdade {self.nome}: ")
		i = 1
		for nome in self.cursos:
			print(f"[{i}] {nome}")
			i = i+1

cursos = [
	'Administração',
	'Design',
	'Enfermagem',
	'Engenharia da Computação',
	'Estética',
	'Física',
	'Matemática',
	'Medicina',
	'Nutrição',
	'Pedagogia',
	'Sistemas de Informação',
]

faculdades = []

faculdades.append(
	Facul("Newton",
		[
		cursos[0],
		cursos[1],
		cursos[2],
		cursos[3],
		]
	)
)

faculdades.append(
	Facul("Enciclopédia",
		[
		cursos[3],
		cursos[4],
		cursos[6],
		cursos[8],
		]
	)
)

faculdades.append(
	Facul("Atenas",
		[
		cursos[0],
		cursos[4],
		cursos[7],
		cursos[9],
		]
	)
)

# Problema: ao escolher o curso, tem que exibir a nota de corte, quantas vagas tem para as bolsas e qual é a faculdade e cidade.
#opcao = int(input('Escolha um curso: '))
#if opcao == 1:
#    print('Administração')'''
