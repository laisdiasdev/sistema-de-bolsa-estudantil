import validate_cpf

class Usuario:
	def __init__(self):
		self.obterDados()

	def obterDados(self):
		self.nome = input("Nome completo do usuário: ")
		self.validarCPF()
		self.enem = int(input("Nota do ENEM: "))
		self.obterRenda()
		self.calcularDesconto()

	def validarCPF(self):
		while True:
			self.cpf = input("CPF do usuário: ")
			if validate_cpf.is_valid(self.cpf) == True:
				break
			else:
				print("Este não é um CPF válido.")

	def obterRenda(self):
		## calcular renda
		pessoas = int(input("Quantas pessoas moram com você? "))
		salarios = []
		for i in range(1, pessoas+1):
			salarios.append(float(input(f"Qual o salário da {i}º pessoa? ")))
		self.renda = sum(salarios)/pessoas
		print(f"A renda de sua família é de R${self.renda}.")

	def calcularDesconto(self):
		self.desconto = 0
		if self.renda <= 1818:
			self.desconto = 100
		elif self.renda <= 2424:
			self.desconto = 75
		elif self.renda <= 3636:
			self.desconto = 50
		elif self.renda <= 6060:
			self.desconto = 25

		if self.desconto > 0:
			print(f"De acordo com sua renda familiar, você pode concorrer à bolsas de {self.desconto}% de desconto.\n")
