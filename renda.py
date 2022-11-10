soma = 0
i = 0
quant_pessoas = int(input("Quantas pessoas moram com você? "))
while i < quant_pessoas:
    i = i + 1 
    salario = float(input(f"Informe a renda da {i}º pessoa: "))
    soma = soma + salario
    renda_familiar = soma/quant_pessoas
print()
print("Sua renda per capta familiar é de R$","%.2f" %renda_familiar)
print()

'''if renda_familiar <= 1818:
    des100 = int(100)
    print("De acordo com sua renda, você pode concorrer a bolsa de 100%")
if (renda_familiar > 1818) and (renda_familiar <= 2424):
    des75 = int(75)
    print("De acordo com sua renda, você pode concorrer a bolsa de 75%")
if (renda_familiar > 2424) and (renda_familiar <= 3636):
    des50 = int(50)
    print("De acordo com sua renda, você pode concorrer a bolsa de 50%")
if (renda_familiar > 3636) and (renda_familiar <= 6060):
    print("De acordo com sua renda, você pode concorrer a bolsa de 25%")'''

    #criar uma classe pra cada curso, mas talvez não seja a melhor opção
class adm :
        def __init__(self):
            self.cem = '4 vagas'
            self.corte1 = '574'
            self.set_cinco = '6 vagas'
            self.metade = '8 vagas'
            self.vinte_cinco = '10 vagas'
        pass
      

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
if opcao == 1:
    print('Administração')
    if renda_familiar <= 1818:
    #des100 = int(100)
        print("De acordo com sua renda, você pode concorrer a bolsa de 100%")
if (renda_familiar > 1818) and (renda_familiar <= 2424):
    #des75 = int(75)
    print("De acordo com sua renda, você pode concorrer a bolsa de 75%")
if (renda_familiar > 2424) and (renda_familiar <= 3636):
    #des50 = int(50)
    print("De acordo com sua renda, você pode concorrer a bolsa de 50%")
if (renda_familiar > 3636) and (renda_familiar <= 6060):
    print("De acordo com sua renda, você pode concorrer a bolsa de 25%")
    

    dados = adm()
    print (dados.cem, dados.corte1)
    #tentei imprimir aqui e não deu
    

'''a intenção depois de saber qual a bolsa é:
mostrar a quantidade de vagas;
nota de corte;
nota do enem do usuário.
Isso pra cada curso ecolhido.'''



'''if des100 == 100:
        print (f'Bolsa de {des100}%')
        dados = adm()
        print (dados.cem,dados.corte1)'''