# Текстовая переменная
res = "Это число "
# Вводится текст
txt = input("Введите название числа от 1 до 4: ")
# Преобразование текста внутри в нижний регистр
txt = txt.lower()
# Идентификация числа
if txt == "один" or txt == "единица":
    res += "1"
elif txt == "два" or txt == "двойка":
    res += "2"
elif txt == "три" or txt == "тройка":
    res += "3"
else:
    res += "не идентифицировано"
# Результат идентификации
print(res)
