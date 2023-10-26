# Функции с документированием
def show(txt):
    "Это функция show() с одним аргументом"
    print("Единственный аргумент:", txt)


def display(a, b):
    "Это функция display() с двумя аргументами"
    print("[1] Первый аргумент:", a)
    print("[2] Первый аргумент:", b)


# Функция без документирования
def hello():
    print("Привет всем!")


# Вызов функций и проверка документирования
print(show.__doc__)
show("A")
print(display.__doc__)
display("B", "C")
# Переменная ссылается на функцию
f = show
# Вызов функции и проверка документирования
print(f.__doc__)
f("D")
# Новый текст документирования для функции
display.__doc__= "Новый текст для display()"
# Проверка результата
print(display.__doc__)
display("E", "F")
# Создается документирование для функции
hello.__doc__ = "Функция hello()"
# Проверка результата
print(hello.__doc__)
hello()