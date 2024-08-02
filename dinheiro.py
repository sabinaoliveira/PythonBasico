contador = 1
quantidade = int(input("Quantas vezes você quer converter? "))
while contador <= quantidade:
    real = float(input("Quantos reais eu tenho? R$ "))
    dolar = real/2.20
    print("Eu tenho US$ ",dolar)
    contador = contador + 1