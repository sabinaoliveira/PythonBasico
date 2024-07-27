L1 = int(input("Digite o valor do lado 1: "))
L2 = int(input("Digite o valor do lado 2: "))
L3 = int(input("Digite o valor do lado 3: "))


if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    if L1 == L2 and L2 == L3:
        print("Este triângulo é equilátero.")
    elif L1 != L2 and L2 != L3 and L1 != L3:
        print("Este triângulo é escaleno.")
    else:
        print("Este triângulo é isósceles.")
else:
    print("Não é um triângulo.")

    
