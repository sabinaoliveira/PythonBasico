numero = int(input("Digite um número: "))
soma = numero
while numero > 1:
    print(numero)
    soma = soma * (numero - 1)
    numero = numero - 1
print("A soma é: ",soma)