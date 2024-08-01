N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
media = (N1 + N2) / 2
print("A média do aluno é:",media)
if media >= 7:
    print("Aluno aprovado!")
else:
    if (media >= 5) & (media < 7):
        print("Aluno em recuperação!")
    else:
        print("Aluno reprovado!")



