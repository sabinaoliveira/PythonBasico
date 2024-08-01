peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura ** 2)
print("IMC:",IMC)
if IMC < 17:
    print("Muito abaixo do peso")
else:
    if (IMC >= 17) & (IMC <= 18.5):
        print("Abaixo do peso")
    else:
        if (IMC >= 18.5) & (IMC < 25):
            print("Peso ideal")
        else:
            if (IMC >= 25) & (IMC < 30):
                print("Sobrepeso")
            else:
                if (IMC >= 30) & (IMC < 35):
                    print("Obesidade")
                else:
                    if (IMC >= 35) & (IMC < 40):
                        print("Obesidade severa")
                    else:
                        print("Obesidade mórbida")
