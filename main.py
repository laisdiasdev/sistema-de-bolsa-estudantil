from classes import Usuario
from dados import faculdades
from dados import cursos

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
	curso = cursos[escolha-1]

	# mostrar bolsas disponíveis
	print("\nDe acordo com sua renda familiar e nota do ENEM, você pode concorrer às seguintes bolsas:")
	i = 1
	for bolsa in curso.bolsas:
		if (bolsa.desconto <= usr.desconto) and (bolsa.n_corte < usr.enem):
			print(f"[{i}] Bolsa de {bolsa.desconto}% de desconto, com nota de corte de {bolsa.n_corte} e {bolsa.vagas} vagas.")
			i = i+1

	# informar usuario caso esteja concorrendo

if __name__ == "__main__":
	main()
