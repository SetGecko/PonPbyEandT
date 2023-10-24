# Функции генераторы
def names():
    yield "Дядя Фёдор"
    yield "Пёс Шарик"
    yield "Кот Матроскин"


def colors():
    L = ["Красный", "Жёлтый", "Зелёный", "Синий"]
    for clr in L:
        yield clr


def myrange(n):
    for k in range(n):
        yield 2*k+1


# использование функций генераторов