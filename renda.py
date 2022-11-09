soma = 0
i = 0
quant_pessoas = int(input("Quantas pessoas moram com você? "))
while i < quant_pessoas:
    i = i + 1 
    salario = float(input(f"Informe a renda da {i}º pessoa: "))
    soma = soma + salario
    renda_familiar = soma/quant_pessoas
print("Sua renda per capta familiar é de R$","%.2f" %renda_familiar)

if renda_familiar <= 1212:
    print("Você pode concorrer a bolsa de 100%")
if (renda_familiar > 1212) and (renda_familiar <= 2424):
    print("Você pode concorrer a bolsa de 75%")
if (renda_familiar > 2424) and (renda_familiar <= 3636):
        print("Você pode concorrer a bolsa de 50%")
if (renda_familiar > 3636) and (renda_familiar <= 6060):
        print("Você pode concorrer a bolsa de 25%")