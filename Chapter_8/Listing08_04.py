# Описание класса
class MyClass:
    # Конструктор
    def __init__(self, n="Белый"):
        self.name = n
        print("Создан объект:", self.name)
    # Деструктор
    def __del__(self):
        print("Удалён объект:", self.name)
# Функция


def create(n):
    obj = MyClass(n)


# Создание объектов
A = MyClass()
B = MyClass("Красный")
C = MyClass("Синий")
# Вызов функции
create("Жёлтый")
# Полю присваивается новое значение
C.name = "Зелёный"
# Удаление объектов
del A
del B
del C
create("Жопка")
