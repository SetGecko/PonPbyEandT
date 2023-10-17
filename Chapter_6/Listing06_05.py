# Функции
def shift(val):
    print("Функция shift()")
    print("Исходное значение:", val)
    val = ["A", "B", "C", "D"]
    print("Конечное значение:", val)


def change(val):
    print("Функция change()")
    print("Исходное значение:", val)
    if type(val) == list:
        for k in range(len(val)):
            val[k] += 1
    else:
        val += 1
    print("Конечное значение:", val)


# Переменная
num = 100
# Список
L = [10, 20, 30]
print(f"Переменная num = {num}")
change(num)
print(f"Переменная num = {num}")
print(f"Список L = {L}")
shift(L)
print(f"Список L = {L}")
change(L)
print(f"Список L = {L}")
