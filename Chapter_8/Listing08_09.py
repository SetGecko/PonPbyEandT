# Импорт функций
from copy import *
# Описание класса
class MyClass:
    pass
# Создание объекта
A = MyClass()
# Поля объекта
A.value = 100
A.nums = [1, 2, 3]
# Присваивание ссылки на объект
B = A
# Копия объекта
C = copy(A)
# Полная копия объекта
D = deepcopy(A)
print("Созданы объекты")
# Поля объектов
print("A:", A.value, "и", A.nums)
print("B:", A.value, "B", A.nums)
print("C:", A.value, "C", A.nums)
print("D:", A.value, "D", A.nums)
print("A.value = 200 и A.nums[1] = 0")
# Новые значения для полей
A.value = 200
A.nums[1] = 0
# Поля объектов
print("A:", A.value, "и", A.nums)
print("B:", B.value, "B", B.nums)
print("C:", C.value, "C", C.nums)
print("D:", D.value, "D", D.nums)
print("Удаляется А")
# Удаление переменной
del A
print("B.value = 300 и B.nums[2] = 4")
# Новые значения для полей
print("B:", B.value, "B", B.nums)
print("C:", C.value, "C", C.nums)
print("D:", D.value, "D", D.nums)
