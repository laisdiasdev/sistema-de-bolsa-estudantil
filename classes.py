class Usuario:
	def __init__(self):
		# perguntar dados do usário
		self.nome = input("Nome do usuário: ")
		self.enem = input("Nota do ENEM: ")

		# calcular renda
		pessoas = int(input("Quantas pessoas moram com você? "))
		salarios = []
		for i in range(1, pessoas+1):
			salarios.append(float(input(f"Qual o salário da {i}º pessoa? ")))
		self.renda = sum(salarios)/pessoas
		print(f"A renda de sua família é de R${self.renda}.")


class Bolsa:
	def __init__(self, vagas, n_corte):
		self.vagas = vagas
		self.n_corte = n_corte


class Curso:
	def __init__(self, nome, bolsas):
		self.nome = nome
		self.bolsas = bolsas


class Facul:
	def __init__(self, nome, cursos):
		self.cursos = cursos
		self.nome = nome
	pass

	def mostrarCursos(self):
		print(f"\nCursos disponíveis na faculdade {self.nome}: ")
		i = 1
		for curso in self.cursos:
			print(f"[{i}] {curso.nome}")
			i = i+1
