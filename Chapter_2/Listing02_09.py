# Вводятся параметры уравнения
a, b = eval(input("Введите через запятую 2 числа: "))
# Если параметры некорректные
if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
    print("Введены некорректные значения!")
    # Завершение выполнения программы
    raise SystemExit(0)
# Если первый параметр ненулевой
elif a != 0:
    txt = "Решение х = " + str(b/a)
# Если второй параметр ненулевой
elif b != 0:
    txt = "Решений нет!"
# Если оба параметра нулевые
else:
    txt = "Решение - любое число"
# Вид уравнения
print("Уравнение " + str(a) + "x=" + str(b))
# Результат поиска корня
print(txt)
print("Поиск решения завершён")
