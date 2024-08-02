# # numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # range primeiro numero eh start, stop depois step (incremento ou decremento)
# for item in range(10,1,-1):
#   print(item)

# contador = 1
# soma = 0 
# while (contador <= 5):
#     numero = float(input("Digite um número: "))
#     soma = soma + numero
#     contador = contador + 1
# print("A soma dos valores é: ",soma)

soma = 0
for numero in range(5):
    numero = float(input("Digite um número: "))
    soma = soma + numero
print("A soma dos valores é: ",soma)