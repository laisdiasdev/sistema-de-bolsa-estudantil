#pedir a renda no início 
#mostrar qual bolsa pode concorrer 
#mostrar os cursos disponíveis
#pedir pra escolher o curso
#mostrar em qual faculdade tem e qual o polo da faculdade

class cursos :
    def __init__(self):
        self.curso1 = 'Engenharia da Computação'
        self.curso2 = 'Pedagogia'
        self.curso3 = 'Estética'
        self.curso4 = 'Sistemas de Informação'
        self.curso4 = 'Medicina'
        self.curso5 = 'Enfermagem'
        self.curso6 = 'Nutrição'
        self.curso7 = 'Matemática'
        self.curso8 = 'Física'
        self.curso9 = 'Administração'
        self.curso10 = 'Design'
        
    pass

faculdade1 = cursos( )
print(faculdade1.curso1,',',faculdade1.curso2,',',faculdade1.curso3,',',faculdade1.curso4)

faculdade2 = cursos( )
print(faculdade1.curso4,',',faculdade1.curso7,',',faculdade1.curso5,',',faculdade1.curso9)

faculdade3 = cursos( )
print(faculdade1.curso10,',',faculdade1.curso8,',',faculdade1.curso5,',',faculdade1.curso1)

class facul :
    def __init__(self):
        self.cursos = [
         'Engenharia da Computação',
         'Pedagogia',
         'Estética',
         'Sistemas de Informação',
         'Medicina',
         'Enfermagem',
         'Nutrição',
         'Matemática',
         'Física',
         'Administração',
         'Design'
         ]
    pass

faculdade1 = facul()

print("Nossos cursos disponíveis são: ")
i = 1
for nome in faculdade1.cursos:
    print(f"[{i}] {nome}")
    i = i+1
#Problema: ao escolher o curso, tem que exibir a nota de corte, quantas vagas tem para as bolsas e qual é a faculdade e cidade.