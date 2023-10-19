# Функции с рекурсивным вызовом
# Функция для вычисления суммы чисел
def mysym(n):
    if n==0:
        return 0
    else:
        return n+mysym(n-1)


# Функция для вычисления чисел Фибоначчи
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# Функция для инверсионного отображения списка/текста
def show(txt):
    if len(txt) == 0:
        print("|")
    else:
        print("|", txt[-1], end="", sep="")
        show(txt[:-1])


# Вызов функций
print("Сумма чисел:")
for k in range(12):
    print(mysym(k), end=" ")
print("\nЧисла Фибоначчи:")
for k in range(15):
    print(fib(k+1), end=" ")
print("\nИнверсия текста:")
show("Hello Python")
print("Инверсия списка")
show([1, 2, 3, 4, 5])
