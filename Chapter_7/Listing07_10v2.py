k = 1
print("Построчное считывание файла")
with open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/Poetry.txt") as fm:
    for L in fm:
        print("["+str(k)+"]", L, end="")
        k = k + 1
print("\nФайл закрыт...")
