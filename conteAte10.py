contador = 0
valor = int(input("Quer contar até quanto? "))
salto = int(input("Qual será o valor do salto? "))
while contador <= valor:
    print("Contador: ",contador)
    contador = contador + salto
print("Terminei de contar!")