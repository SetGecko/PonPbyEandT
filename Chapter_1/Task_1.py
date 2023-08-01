"""
Напишите программу, в которой программа спрашивает у пользователя день и месяц,
а затем выводит сообщение о текущем дне и месяце
"""
from datetime import date
userDate = input("Введите желаемые дату и месяц: ")
currentDate = date.today()
print("Вы ввели дату и месяц: ", userDate)
print("Сегодня", currentDate.day, "число, месяц", currentDate.month)
