nome = input("Digite seu nome: ")
print("Total de letras do seu nome: ",len(nome))
print("Seu nome em maiúsculas é:",nome.upper())
print("Seu nome em minúsculas é:",nome.lower())
print("A primeira letra do seu nome é:",nome[0])
print("A última letra do seu nome é:",nome[-1])
for letra in nome:
    print(ord(letra))

for letra in nome[::-1]:
    print(letra)