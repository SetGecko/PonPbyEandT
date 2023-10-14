# Исходный текст
txt = "Hello python"
print(txt)
# Текст в обратном порядке
A = txt[::-1]
print(A)
# Первое слово в тексте
B = txt[:5]
print(B)
# Последнее слово в тексте
C = txt[6:]
print(C)
# Переменная с текстовым значением
new_txt = ""
# Переменная с целочисленным значением
delta = ord("a") - ord("A")
# Перебор символов в тексе
for s in txt:
    # Если буква в диапазоне от a до z
    if(ord(s) >= ord("a") and ord(s) <= ord("z")):
        s = chr(ord(s)-delta)
    # Добавление символа к тексту
    new_txt += s
# Текст из больших букв
print(new_txt)
