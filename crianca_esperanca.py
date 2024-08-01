print("------------------------------------------------------------")
print("                     CRIANÇA ESPERANÇA                      ")
print("------------------------------------------------------------")
print("                  Muito obrigada por ajudar!                ")
print("[1] para doar R$ 10")
print("[2] para doar R$ 25")
print("[3] para doar R$ 50")
print("[4] para doar outros valores")
print("[5] para cancelar")
doacao = int(input())
match doacao:
    case 1:
        valor = 10
    case 2:
        valor = 25
    case 3:
        valor = 50
    case 4:
        valor = float(input("Qual valor você gostaria de doar? R$ "))
    case 5:
        valor = "cancelar"
    case _:
        valor = "invalida"
if valor == "cancelar":
    print("Cancelado!")
elif valor == "invalida":
    print("Opção inválida!")
else:
    print("-------------------------------------------------------------")
    print("Sua doação foi de R$",valor)
    print("Muito obrigada!")
    print("-------------------------------------------------------------")
