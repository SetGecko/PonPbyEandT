print("Начинается копирование файла")
# Контролируемый код
try:
    # Бинарный файл открывается на чтение
    A = open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/cat.jpg", "rb")
    # Создаётся бинарный файл
    B = open("/Users/setgecko/PycharmProjects/PonPbyEandT/Chapter_7/kitty.jpg", "xb")
    # Содержимое первого файла считывается и копируется во 2 файл
    B.write(A.read())
    # Файлы закрываются
    A.close()
    B.close()
    print("Копирование прошло успешно")
# Если 2 файл уже существует
except FileExistsError:
    print("Ошибка: такой файл уже существует")
except:
    print("Ошибка доступа к файлу")
print("Программа завершила выполнение")
