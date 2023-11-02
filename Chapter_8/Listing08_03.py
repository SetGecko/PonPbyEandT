# Описание класса
class MyClass:
    # Методля присваивания значения полю
    def set(self, n):
        self.number = n

    # Методля отображения значения поля
    def show(self):
        print("Поле number =", self.number)

# Создание объекта
obj = MyClass()
# Проверка наличия поля
print("Наличие поля number:", hasattr(obj, "number"))
try:
    # Проверка значения поля
    obj.show()
except AttributeError:
    print("Поля number нет у объекта!")
# Присваивание значения полю
obj.number = 123
# Проверка наличия поля
print("Наличие поля number:", hasattr(obj, "number"))
# Проверка значения поля
obj.show()
# Новое значение поля
obj.set(321)
# Проверка значения поля
obj.show()
