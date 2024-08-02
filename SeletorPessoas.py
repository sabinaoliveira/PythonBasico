print("===================================================")
print("                SELETOR DE PESSOAS                 ")
print("===================================================")
sexo = input("Qual o sexo? [M/F] ")
idade = int(input("Qual a idade? "))
resposta = input("Você quer continuar? ")
while resposta == "sim":
    print("Qual a cor do cabelo? ")
    print("[1] Preto")
    print("[2] Castanho")
    print("[3] Loiro")
    print("[4] Ruivo")
    cabelo = input()
    match cabelo:
        case 1:
            valor = "preto"
        case 2:
            valor = "castanho"
        case 3:
            valor = "loiro"
        case 4:
            valor = "ruivo"  








