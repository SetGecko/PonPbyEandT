# Описание класса
class MyClass:
    # Поле класса
    color = "Красный"
    # Методы класса
    def set(txt):
        MyClass.color = txt

    def show():
        print(MyClass.color)


# Вызов методов класса
MyClass.show()
MyClass.set("Зелёный")
# Отображение значения поля класса
print(MyClass.color)
# Новое значение для поля класса
MyClass.color = "Синий"
# Создание объектов класса
A = MyClass()
B = MyClass()
# Проверка значения поля
print("Класс:", MyClass.color)
print("Объект А:", A.color)
print("Объект B:", B.color)
# Присваивание значения полю
A.color = "Белый"
# Проверка занчения полем
print("Класс:", MyClass.color)
print("Объект А:", A.color)
print("Объект B:", B.color)
# Присваивание значения поля
MyClass.color = "Жёлтый"
# Проверка значения поля
print("Класс:", MyClass.color)
print("Объект А:", A.color)
print("Объект B:", B.color)
# Удаление поля из объекта А
del A.color
# Проверка значения поля
print("Класс:", MyClass.color)
print("Объект А:", A.color)
print("Объект B:", B.color)
