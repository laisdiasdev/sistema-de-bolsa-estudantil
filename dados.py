from classes import Bolsa
from classes import Curso
from classes import Facul

cursos = [
	Curso("Administração",
		[
		Bolsa(4, 574),
		Bolsa(6, 507),
		Bolsa(8, 483),
		Bolsa(10, 470),
		]
	),
	Curso("Design",
		[
		Bolsa(6, 620),
		Bolsa(8, 593),
		Bolsa(10, 572),
		Bolsa(12, 547),
		]
	),
	Curso("Enfermagem",
		[
		Bolsa(8, 698),
		Bolsa(10, 567),
		Bolsa(14, 572),
		Bolsa(14, 564),
		]
	),
	Curso("Engenharia Da Computação",
		[
		Bolsa(4, 720),
		Bolsa(5, 643),
		Bolsa(4, 582),
		Bolsa(7, 547),
		]
	),
	Curso("Estética",
		[
		Bolsa(8, 604),
		Bolsa(5, 696),
		Bolsa(7, 572),
		Bolsa(7, 547),
		]
	),
	Curso("Fisica",
		[
		Bolsa(0, 0),
		Bolsa(8, 593),
		Bolsa(0, 572),
		Bolsa(12, 547),
		]
	),
	Curso("Matemática",
		[
		Bolsa(5, 532),
		Bolsa(7, 522),
		Bolsa(10, 506),
		Bolsa(12, 479),
		]
	),
	Curso("Medicina",
		[
		Bolsa(7, 807),
		Bolsa(0, 0),
		Bolsa(5, 787),
		Bolsa(0, 0),
		]
	),
	Curso("Nutrição",
		[
		Bolsa(11, 625),
		Bolsa(8, 592),
		Bolsa(10, 563),
		Bolsa(12, 542),
		]
	),
	Curso("Pedagogia",
		[
		Bolsa(9, 680),
		Bolsa(8, 577),
		Bolsa(10, 569),
		Bolsa(12, 533),
		]
	),
	Curso("Sistemas de Informação",
		[
		Bolsa(8, 660),
		Bolsa(7, 594),
		Bolsa(12, 572),
		Bolsa(12, 556),
		]
	),
]

faculdades = [
	Facul("Newton",
		[
		cursos[0],
		cursos[1],
		cursos[2],
		cursos[3],
		]
	),
	Facul("Enciclopédia",
		[
		cursos[3],
		cursos[4],
		cursos[6],
		cursos[8],
		]
	),
	Facul("Atenas",
		[
		cursos[0],
		cursos[4],
		cursos[7],
		cursos[9],
		]
	)
]
