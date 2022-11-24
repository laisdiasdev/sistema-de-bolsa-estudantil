from classes.usuario import *
from dados import *

def main():
	# cadastro do usuario
	usr = Usuario()

	# mostrar faculdades disponíveis
	print("As faculdades disponíveis são:")
	i = 1
	for facul in faculdades:
		print(f"[{i}] Faculdade {facul.nome}")
		i = i+1

	# escolher uma faculdade
	while True:
		escolha = int(input("\nEm qual faculdade você deseja se matricular? "))
		if (escolha > 0 and escolha <= len(faculdades)):
			break
		else:
			print("\nDigite um número válido.")
	facul = faculdades[escolha-1]

	# escolher um curso
	facul.mostrarCursos()
	while True:
		escolha = int(input("\nEm qual curso você deseja se matricular? "))
		if (escolha > 0 and escolha < len(facul.cursos)):
			break
		else:
			print("\nEste não é um número válido.")
	usr.curso = cursos[escolha-1]

	# calcular a qual bolsa o usuario pode concorrer
	i = 1
	for bolsa in usr.curso.bolsas:
			if (bolsa.desconto == usr.desconto):
				print("\nDe acordo com sua renda per capta familiar e nota do ENEM, você pode concorrer à seguinte bolsa:")
				print(f"[{i}] Bolsa de {bolsa.desconto}% de desconto, com nota de corte de {bolsa.n_corte} e {bolsa.vagas} vagas.")
			i = i+1
	else:
		if (bolsa.n_corte > usr.enem):
			print("\nPorém, sua nota do ENEM é menor do que a nota de corte do curso. Você pode paticipar da lista de espera após o resultado.")

	# informar usuario caso esteja concorrendo

if __name__ == "__main__":
	main()
	def opcoes(self):
		self.opcao = input("Deseja concorrer à bolsa? (SIM/NAO)")
		if self.opcao == "SIM":
			print("Parabéns! Você está concorrendo à bolsa. Aguarde a convocação no edital que será lançado.")
		else: 
			print("ENCERRADO")
