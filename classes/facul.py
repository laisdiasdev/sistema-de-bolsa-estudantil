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
