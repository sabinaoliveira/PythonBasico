N = int(input("Digite um número: "))
def fatorial(V):
    resultado = 1
    for contador in range(1,V+1):
        resultado = resultado * contador
    return resultado
F = fatorial(N)
print(f"O valor de {N}! é igual a: {F}")


