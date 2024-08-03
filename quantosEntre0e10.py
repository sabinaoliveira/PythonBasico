total = 0
somaImp = 0
for contador in range(6):
    valor = int(input("Digite um valor: "))
    if valor >= 0 and valor <= 10:
        total = total + 1
        if valor %2 == 1:
            somaImp = somaImp + valor
print("Ao todo foram",total,"valores entre 0 e 10")
print("Nesse intervalo, a soma de ímpares foi: ",somaImp)

