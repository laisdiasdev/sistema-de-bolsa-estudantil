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
