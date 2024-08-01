peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura ** 2)
print("IMC:",IMC)
if (IMC >= 18.5) & (IMC < 25):
    print("Parabéns! Você está no seu peso ideal.")
else:
    print("Você não está na faixa de peso ideal.")