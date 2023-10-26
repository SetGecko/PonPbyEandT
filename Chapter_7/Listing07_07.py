# Импорт класса из модуля
from datetime import date
# Объект для реализации даты
mydate = date(2023, 10, 26)
# Проверка резульатата
print("Первая дата:", mydate)
# Использование полей объекта
print("Год:", mydate.year)
print("Месяц:", mydate.month)
print("День", mydate.day)
# Определение дня недели
print("День недели:", mydate.weekday())
print("День недели:", mydate.isoweekday())
# Создание нового объекта на основе существующего
newdate = mydate.replace(1985, day=15)
# Проверка резульатата
print("Вторая дата:", newdate)
# Созданиие нового объекта
newdate = date.fromisoformat("1998-08-12")
# Проверка результата
print("Новая дата:", newdate)
thisday = date.today()
# Проверка результата
print("Сегодня:", thisday)
# Разность дат
delta = mydate - newdate
# Проверка результата
print("До первой даты:", delta)

