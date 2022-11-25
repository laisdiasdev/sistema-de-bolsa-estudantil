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

	# remover 1 pois listas começam no número 0
	usr.facul = faculdades[escolha-1]

	# escolher um curso
	usr.facul.mostrarCursos()
	while True:
		escolha = int(input("\nEm qual curso você deseja se matricular? "))
		if (escolha > 0 and escolha <= len(usr.facul.cursos)):
			break
		else:
			print("\nEste não é um número válido.")

	# remover 1 pois listas começam no número 0
	usr.curso = usr.facul.cursos[escolha-1]

	print(f"\nVocê se cadastrou no curso de {usr.curso.nome} na faculdade {usr.facul.nome}.")

	# calcular a qual bolsa o usuario pode concorrer
	i = 1
	for bolsa in usr.curso.bolsas:
		if (bolsa.desconto == usr.desconto):
			if (bolsa.n_corte <= usr.enem):
				print("\nDe acordo com sua renda per capta familiar e nota do ENEM, você pode concorrer à seguinte bolsa:")
				print(f"Bolsa de {bolsa.desconto}% de desconto, com nota de corte de {bolsa.n_corte} e {bolsa.vagas} vagas.")
				escolha = input("\nDeseja concorrer à bolsa? (S/N) ")
				if (escolha == "sim" or escolha == "s" or escolha == "S"):
					usr.bolsa = bolsa
			else:
				escolha = input("\nSua nota do ENEM é menor do que a nota de corte do curso. Você deseja paticipar da lista de espera? (S/N) ")
				if (escolha == "sim" or escolha == "s" or escolha == "S"):
					print("Você está cadastrado na lista de espera, o contataremos após a saída dos resultados.")
					return
			break
		i = i+1

	print(f"Parabéns, você está matriculado no curso de {usr.curso.nome} na faculdade {usr.facul.nome}.")

if __name__ == "__main__":
	main()
