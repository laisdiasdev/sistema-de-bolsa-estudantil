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

faculNewton = cursos( )
print(faculNewton.curso1,',',faculNewton.curso2,',',faculNewton.curso3,',',faculNewton.curso4)

faculEnciclopedia = cursos( )
print(faculEnciclopedia.curso4,',',faculEnciclopedia.curso7,',',faculEnciclopedia.curso5,',',faculEnciclopedia.curso9)

faculAtenas = cursos( )
print(faculAtenas.curso10,',',faculAtenas.curso8,',',faculAtenas.curso5,',',faculAtenas.curso1)

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