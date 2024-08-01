nome = input("Qual o nome do funcionário? ")
salario = float(input("Qual o salário do funcionário? "))
dependente = int(input("Qual a quantidade de dependentes? "))
novoSalario = salario + dependente
match dependente:
    case 0:
        novoSalario = salario + (salario*5/100)
    case 1, 2, 3:
        novoSalario = salario + (salario*10)/100
    case 4, 5, 6:
        novoSalario = salario + (salario*15/100)
    case _:
        novoSalario = salario + (salario*18/100)
        print("O novo salário é R$ ",novoSalario)



