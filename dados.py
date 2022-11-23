from classes.curso import *
from classes.bolsa import *
from classes.facul import *

cursos = [
	Curso("Administração",
		[
		Bolsa(100, 4, 574),
		Bolsa(75, 6, 507),
		Bolsa(50, 8, 483),
		Bolsa(25, 10, 470),
		]
	),
	Curso("Design",
		[
		Bolsa(100, 6, 620),
		Bolsa(75, 8, 593),
		Bolsa(50, 10, 572),
		Bolsa(25, 12, 547),
		]
	),
	Curso("Enfermagem",
		[
		Bolsa(100, 8, 698),
		Bolsa(75, 10, 567),
		Bolsa(50, 14, 572),
		Bolsa(25, 14, 564),
		]
	),
	Curso("Engenharia Da Computação",
		[
		Bolsa(100, 4, 720),
		Bolsa(75, 5, 643),
		Bolsa(50, 4, 582),
		Bolsa(25, 7, 547),
		]
	),
	Curso("Estética",
		[
		Bolsa(100, 8, 604),
		Bolsa(75, 5, 696),
		Bolsa(50, 7, 572),
		Bolsa(25, 7, 547),
		]
	),
	Curso("Fisica",
		[
		Bolsa(100, 4, 604),
		Bolsa(75, 8, 593),
		Bolsa(50, 0, 572),
		Bolsa(25, 12, 547),
		]
	),
	Curso("Matemática",
		[
		Bolsa(100, 5, 532),
		Bolsa(75, 7, 522),
		Bolsa(50, 10, 506),
		Bolsa(25, 12, 479),
		]
	),
	Curso("Medicina",
		[
		Bolsa(100, 7, 807),
		Bolsa(75, 6, 798),
		Bolsa(50, 5, 787),
		Bolsa(25, 0, 0),
		]
	),
	Curso("Nutrição",
		[
		Bolsa(100, 11, 625),
		Bolsa(75, 8, 592),
		Bolsa(50, 10, 563),
		Bolsa(25, 12, 542),
		]
	),
	Curso("Pedagogia",
		[
		Bolsa(100, 9, 680),
		Bolsa(75, 8, 577),
		Bolsa(50, 10, 569),
		Bolsa(25, 12, 533),
		]
	),
	Curso("Sistemas de Informação",
		[
		Bolsa(100, 8, 660),
		Bolsa(75, 7, 594),
		Bolsa(50, 12, 572),
		Bolsa(25, 12, 556),
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
	Facul("Jacques Rousseau",
		[
		cursos[3],
		cursos[4],
		cursos[6],
		cursos[8],
		]
	),
	Facul("Saint Louis",
		[
		cursos[0],
		cursos[4],
		cursos[7],
		cursos[9],
		]
	)
]
