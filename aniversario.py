ano_atual = int(input("Em que ano nós estamos? "))
mes_atual = int(input("Em que mês nós estamos? "))
ano_nasc = int(input("Em que ano eu nasci? "))
mes_nasc = int(input("Em que mês eu nasci? "))
idade = ano_atual - ano_nasc
if mes_atual >= mes_nasc:
    print("Minha idade é: ",idade)
else:
    print("Minha idade é: ",idade -1)
