'''vagas1 = bolsa de 100% e notaDeCorte1 = nota de corte dessa bolsa
vagas2 = bolsa de 75% e notaDeCorte2 = nota de corte dessa bolsa
etc.'''

class facul :
    def __init__(self):
        self.cursos = [
         'Administração',
         'Design',
         'Enfermagem',
         'Engenharia da Computação',
         'Estética',
         'Física',
         'Matemática',
         'Medicina',
         'Nutrição',
         'Pedagogia',
         'Sistemas de Informação',
         ]
pass

faculdade1 = facul()
print()
print("Nossos cursos disponíveis são: ")
i = 1
for nome in faculdade1.cursos:
    print(f"[{i}] {nome}")
    i = i+1
opcao = int(input('Escolha um curso: '))
#cursos = ["Administração", "Design", "Enfermagem", "Engenharia da Computação", "Estética", "Física", "Matemática", "Medicina",  "Nutrição", "Pedagogia", "Sistemas de Informação"]
#if opcao == 1:
    #print(facul[0])

'''
vagas1 = bolsa de 100% e notaDeCorte1 = nota de corte dessa bolsa
vagas2 = bolsa de 75% e notaDeCorte2 = nota de corte dessa bolsa
etc.'''
class Dados:
        def __init__(self, curso, vagas1,notaDeCorte1,vagas2,notaDeCorte2,vagas3,notaDeCorte3,vagas4,notaDeCorte4):
            self.curso = curso
            self.vagas1 = vagas1
            self.notaDeCorte1 = notaDeCorte1
            self.vagas2 = vagas2
            self.notaDeCorte2 = notaDeCorte2
            self.vagas3 = vagas3
            self.notaDeCorte3 = notaDeCorte3
            self.vagas4 = vagas4
            self.notaDeCorte4 = notaDeCorte4
        pass


Administracao = Dados(
    '4 vagas',
    '574',
    '6 vagas',
    '507',
    '8 vagas',
    '483',
    '10 vagas',
    '470'
    )