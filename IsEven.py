N = int(input("Digite um número: "))
def IsEven(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print("O número digitado é par?",IsEven(N))
