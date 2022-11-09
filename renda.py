soma = 0
i = 0
quant_pessoas = int(input("Quantas pessoas moram com você? "))
while i < quant_pessoas:
    i = i + 1 
    salario = float(input(f"Informe a renda da {i}º pessoa: "))
    soma = soma + salario
    rendafamiliar = soma/quant_pessoas
print("Sua renda per capta familiar é de R$","%.2f" %rendafamiliar)

if rendafamiliar <= 1212:
    print("Você pode concorrer a bolsa de 100%")
if (rendafamiliar > 1212) and (rendafamiliar <= 2424):
    print("Você pode concorrer a bolsa de 75%")
if (rendafamiliar > 2424) and (rendafamiliar <= 3636):
        print("Você pode concorrer a bolsa de 50%")
if (rendafamiliar > 3636) and (rendafamiliar <= 6060):
        print("Você pode concorrer a bolsa de 25%")