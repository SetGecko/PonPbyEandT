# Функция с 3 аргументами
def show(first, second, third):
    print(f"[1] Первый аргумент - {first}")
    print(f"[2] Второй аргумент - {second}")
    print(f"[3] Третий аргумент - {third}")


# Вызов функции
show(1, 2, 3)
show(second="B", third="C", first="A")
show(1, third=3, second=2)
