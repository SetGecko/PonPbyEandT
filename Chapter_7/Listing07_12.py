# Считывается текст
txt = input("Ввдеите текст:")
# Файл открывается для записи
mf = open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/mytext.txt", 'w')
# Текст записывается в файл
mf.write(txt)
# Закрываем файл
mf.close()
# Сообщение о завершении копирования
print("Текст записан в файл")
