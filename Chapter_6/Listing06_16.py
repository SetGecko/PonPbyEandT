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


# Использование функций генераторов
print("Они из Простоквашино:")
for name in names():
    print(name)
print(list(names()))
R = colors()
print("Цветовой спектр:")
for r in R:
    print(r, end=" ")
print("\nЕщё одна попытка...")
for r in R:
    print(r, end=" ")
print("Ничего нет? Этонормально.")
print("Нечётные числа")
print(list(myrange(10)))
print(tuple(myrange(10)))
N = myrange(8)
A = list(N)
print("A =", A)
B = list(N)
print("B =", B)
for num in myrange(8):
    print(num, end=" ")
print()

