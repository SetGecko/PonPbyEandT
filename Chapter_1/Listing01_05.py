# Текстовое представление команды:
txt = "(2 + 3) / 0.25 - 4 * 2.1"
# Отображение выражения и вычисления результата:
print(txt, "=", eval(txt))
# Считывание выражения для вычисления:
res = input("Введите выражение: ")
# Отображение значения выражения:
print("Значение выражения: ", eval(res))
