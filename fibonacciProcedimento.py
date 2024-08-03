def Fibonacci(numero1,numero2):
    soma = numero1 + numero2
    numero1 = numero2
    return numero2, soma
T1 = 0
T2 = 1
for _ in range(10+1):
    T1, T2 = Fibonacci(T1,T2)
    print(T2)