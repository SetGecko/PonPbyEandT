# Первый класс
class Alpha:
    pass


# Второй класс
class Bravo:
    name = "Bravo"

    def display():
        print("Поле name:", Bravo.name)

    def show(self):
        print("Поле value:", self.value)

    def __init__(self):
        self.value = 123


# Создание объектов
A = Alpha()
B = Bravo()
# Атрибуты первого класса
print("Класс Alpha")
n = 1
for s in Alpha.__dict__:
    print("[" + str(n) + "] " + s + ":", Alpha.__dict__[s])
    n = n + 1
# Атрибуты второго класса
print("Класс Bravo")
n = 1
for s in Bravo.__dict__:
    print("[" + str(n) + "] " + s + ":", Bravo.__dict__[s])
    n = n + 1
# Атрибуты объектов
print("Объект А:", A.__dict__)
print("Объект B:", B.__dict__)
# Вызов методов класса
Bravo.display()
# Создание атрибутов класса
Alpha.display = Bravo.display
# Удаление атрибута класса
del Bravo.display
# Вызов метода из объекта
B.show()
# Создание атрибута класса
A.color = "Красный"
# Создание атрибута объекта
B.show = lambda: print("Объект В:", B.value)
# Атрибуты первого класса
print("Класс Alpha")
n = 1
for s in Alpha.__dict__:
    print("[" + str(n) + "] " + s + ":", Alpha.__dict__[s])
    n = n + 1
# Атрибуты второго класса
print("Класс Bravo")
n = 1
for s in Bravo.__dict__:
    print("[" + str(n) + "] " + s + ":", Bravo.__dict__[s])
    n = n + 1
# Атрибуты объектов
print("Объект А:", A.__dict__)
print("Объект B:", B.__dict__)
# Вызов методов
Alpha.display()
Bravo.show(B)
B.show()

