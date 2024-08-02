soma = 0
resposta = "sim"
while resposta == "sim":
    numero = int(input("Digite o valor: "))
    soma = soma + numero
    resposta = str(input("Você quer continuar? "))
print("A soma de todos os valores é: ",soma)
