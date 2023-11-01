# Открываем текстовый файл для чтения
mf = open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/Poetry.txt")
# Считывается содержимое файла
txt = mf.read()
print("Содержимое файла:")
# Отображения содержимого файла
print(txt)
# Закрываем файл
mf.close()
print("Файл закрыт...")
