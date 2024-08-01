ano_atual = int(input("Em que ano nós estamos? "))
mes_atual = int(input("Em que mês nós estamos? "))
ano_nasc = int(input("Em que ano você nasceu? "))
mes_nasc = int(input("Em que mês você nasceu? "))
idade = ano_atual - ano_nasc
if mes_atual >= mes_nasc:
    print("Sua idade é: ",idade)
else:
    print("Sua idade é: ",idade -1)
