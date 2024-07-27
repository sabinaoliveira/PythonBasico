emprestimo = float(input("Qual o valor do empréstimo? "))
parcela = int(input("Em quantas parcelas você quer fazer? "))
juros = emprestimo*(20/100)

print("O valor da parcela será: R$ ",(emprestimo+juros)/parcela)