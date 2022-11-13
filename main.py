from usuario import Usuario
from faculdade import Facul
from faculdade import faculdades

def mostrarFaculdades():
	i = 1
	for facul in faculdades:
		print(f"[{i}] Faculdade {facul.nome}")
		i = i+1

def main():
	# cadastro do usuario
	#usr = Usuario()

	# mostrar faculdades disponíveis
	confirma = "n"
	while confirma != "s":
		mostrarFaculdades()
		facul = faculdades[int(input("\nEm qual faculdade você deseja se matricular? "))-1]
		facul.mostrarCursos()
		confirma = input(f"\nDeseja se matricular na faculdade {facul.nome}? (s/N) ")

	# escolher curso, instituicao e turno
	# mostrar bolsas disponíveis
	# informar usuario caso esteja concorrendo

if __name__ == "__main__":
	main()
