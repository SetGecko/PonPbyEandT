# Функция с разными аргументами
def my_sum(n, *a, txt="Сумма чисел"):
    s = 0
    for m in range(len(a)):
        s += a[m] ** n
    print(txt+":", s)


# Вызов функции
my_sum(1, 100, 200, 300)
my_sum(2, 10, 20, 30, txt="Сумма квадратов")
