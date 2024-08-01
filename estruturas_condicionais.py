dinheiro = int(input("Quanto nós temos? "))
if dinheiro >= 10000:
    print("Partiu Disney!")
else:
    if (dinheiro >= 5000) & (dinheiro < 10000):
        print("Vou visitar a família!")
    else:
        print("Que tristeza!")
