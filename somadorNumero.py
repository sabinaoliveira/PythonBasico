contador = 1
soma = 0
maior = 0
menor = 0
while contador <= 3:
    numero = int(input(f"Digite o {contador} º valor: "))
    if numero > maior:
        maior = numero
    if contador == 1:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    soma = soma + numero 
    contador = contador + 1
print("A soma de todos os valores é: ",soma)
print("O maior valor é: ",maior)
print("O menor valor é: ",menor)