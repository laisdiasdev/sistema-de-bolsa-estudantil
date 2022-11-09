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

print("Nossos cursos disponíveis são: ")
print('[1] Administração')
print('[2] Design')
print('[3] Enfermagem')
print('[4] Engenharia da Computação')
print('[5] Estética')
print('[6] Física')
print('[7] Matemática')
print('[8] Medicina')
print('[9] Nutrição')
print('[10] Pedagogia')
print('[11] Sistemas de Informação')

opcao = int('Escolha um curso: ')
if (opcao == 1):
    print (faculdade1) #inacabado
