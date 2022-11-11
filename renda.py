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
class Administracao :
        def __init__(self):
            self.cem = '4 vagas'
            self.notaDeCorte1 = '574'
            self.sete_cinco = '6 vagas'
            self.notaDeCorte2 = '507'
            self.metade = '8 vagas'
            self.notaDeCorte3 = '483'
            self.vinte_cinco = '10 vagas'
            self.notaDeCorte4 = '470'
        pass

class Design :
        def __init__(self):
            self.cem = '6 vagas'
            self.notaDeCorte1 = '620'
            self.sete_cinco = '8 vagas'
            self.notaDeCorte2 = '593'
            self.metade = '10 vagas'
            self.notaDeCorte3 = '572'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '547'
        pass

class Enfermagem :
        def __init__(self):
            self.cem = '8 vagas'
            self.notaDeCorte1 = '698'
            self.sete_cinco = '10 vagas'
            self.notaDeCorte2 = '667'
            self.metade = '14 vagas'
            self.notaDeCorte3 = '572'
            self.vinte_cinco = '14 vagas'
            self.notaDeCorte4 = '564'
        pass

class EngenhariaDaComputacao :
        def __init__(self):
            self.cem = '4 vagas'
            self.notaDeCorte1 = '720'
            self.sete_cinco = '5 vagas'
            self.notaDeCorte2 = '643'
            self.metade = '4 vagas'
            self.notaDeCorte3 = '582'
            self.vinte_cinco = '7 vagas'
            self.notaDeCorte4 = '547'
        pass

class Estetica :
        def __init__(self):
            self.cem = '8 vagas'
            self.notaDeCorte1 = '604'
            self.sete_cinco = '5 vagas'
            self.notaDeCorte2 = '596'
            self.metade = '7 vagas'
            self.notaDeCorte3 = '572'
            self.vinte_cinco = '7 vagas'
            self.notaDeCorte4 = '547'
        pass

class Fisica :
        def __init__(self):
            self.cem = '0 vagas'
            self.notaDeCorte1 = ''
            self.sete_cinco = '8 vagas'
            self.notaDeCorte2 = '593'
            self.metade = '0 vagas'
            self.notaDeCorte3 = '572'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '547'
        pass

class Matematica :
        def __init__(self):
            self.cem = '5 vagas'
            self.notaDeCorte1 = '532'
            self.sete_cinco = '7 vagas'
            self.notaDeCorte2 = '522'
            self.metade = '10 vagas'
            self.notaDeCorte3 = '506'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '479'
        pass

class Medicina :
        def __init__(self):
            self.cem = '7 vagas'
            self.notaDeCorte1 = '807'
            self.sete_cinco = '0 vagas'
            self.notaDeCorte2 = ''
            self.metade = '5 vagas'
            self.notaDeCorte3 = '787'
            self.vinte_cinco = '0 vagas'
            self.notaDeCorte4 = ''
        pass

class Nutricao :
        def __init__(self):
            self.cem = '11 vagas'
            self.notaDeCorte1 = '625'
            self.sete_cinco = '8 vagas'
            self.notaDeCorte2 = '592'
            self.metade = '10 vagas'
            self.notaDeCorte3 = '563'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '542'
        pass

class Pedagogia :
        def __init__(self):
            self.cem = '9 vagas'
            self.notaDeCorte1 = '580'
            self.sete_cinco = '8 vagas'
            self.notaDeCorte2 = '577'
            self.metade = '10 vagas'
            self.notaDeCorte3 = '569'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '533'
        pass

class SistemasDeInformacao :
        def __init__(self):
            self.cem = '8 vagas'
            self.notaDeCorte1 = '660'
            self.sete_cinco = '8 vagas'
            self.notaDeCorte2 = '594'
            self.metade = '12 vagas'
            self.notaDeCorte3 = '572'
            self.vinte_cinco = '12 vagas'
            self.notaDeCorte4 = '556'
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
#como posso obter uma lista daqui pra facilitar na escolha
opcao = int(input('Escolha um curso: '))
if opcao == 1:
    print('Administração')
    if renda_familiar <= 1818:



    #des100 = int(100)
        print("De acordo com sua renda per capta familiar, você pode concorrer a bolsa de 100%")
if (renda_familiar > 1818) and (renda_familiar <= 2424):
    #des75 = int(75)
    print("De acordo com sua renda per capta familiar, você pode concorrer a bolsa de 75%")
if (renda_familiar > 2424) and (renda_familiar <= 3636):
    #des50 = int(50)
    print("De acordo com sua renda per capta familiar, você pode concorrer a bolsa de 50%")
if (renda_familiar > 3636) and (renda_familiar <= 6060):
    print("De acordo com sua renda per capta familiar, você pode concorrer a bolsa de 25%")
    

dados = Administracao()
print (dados.cem, dados.notaDeCorte1)
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