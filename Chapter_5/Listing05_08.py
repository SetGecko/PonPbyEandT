txt = "Мы изучаем язык Python"
print(txt)
A = txt.replace(" ", "_*_")
print(A)
B = txt.replace(" ", "\n")
print(B)
C = txt.replace(" ", " не ", 1).replace("Python", "Java")
print(C)
D = txt.replace("язык", "")
print(D)

