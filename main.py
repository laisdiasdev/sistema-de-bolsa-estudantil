from classes import Usuario
from dados import faculdades
from dados import cursos

def main():
	# cadastro do usuario
	usr = Usuario()

	# mostrar faculdades disponíveis
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
			print("\nEste não é um número válido.")
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

	print(f"Você se matriculou no curso de {curso.nome} na faculdade {facul.nome}.")

	# mostrar bolsas disponíveis
	# informar usuario caso esteja concorrendo

if __name__ == "__main__":
	main()
