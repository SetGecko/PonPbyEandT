# Функции
def alpha():
    print("Это Alpha!")


def bravo():
    print("Это Bravo!")


def hello():
    print("А это Hello!")

# Переменная с целочсиленным значением
num = 123
# Вызов функций и проверка значений переменной
print("Сначало было так:")
alpha()
bravo()
hello()
print("num = ", num)
# Изменение значений
alpha, bravo = bravo, alpha
num = hello
hello = 123
# Вызов "функций" и проверка значения переменной
print("А стало так:")
alpha()
bravo()
num()
print("Hello =", hello)
