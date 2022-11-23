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

	# calcular a quais bolsas usuario pode concorrer
	usr.bolsas = []
	for bolsa in usr.curso.bolsas:
		if (bolsa.desconto <= usr.desconto) and (bolsa.n_corte < usr.enem):
			usr.bolsas.append(bolsa)

	# mostrar bolsas disponiveis
	if len(usr.bolsas) > 0:
		i = 1
		print("\nDe acordo com sua renda per capta familiar e nota do ENEM, você pode concorrer às seguintes bolsas:")
		for bolsa in usr.curso.bolsas:
			print(f"[{i}] Bolsa de {bolsa.desconto}% de desconto, com nota de corte de {bolsa.n_corte} e {bolsa.vagas} vagas.")
			i = i+1
	else:
		print("\nDe acordo com sua renda familiar e nota do ENEM, você não pode concorrer à nenhuma bolsa.")

	# informar usuario caso esteja concorrendo

if __name__ == "__main__":
	main()
