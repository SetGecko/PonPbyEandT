# Открываем текстовый файл для чтения
mf = open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/Poetry.txt")
# Переменная для нумерации строк
k = 1
# Построчное считывание файла
print("Построчное считывание файла")
for L in mf:
    # Отображение номера строки и самой строки
    print("["+str(k)+"]", L, end="")
    k = k + 1
# Закрываем файл
mf.close()
print("\nФайл закрыт...")
