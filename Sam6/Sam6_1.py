a = int(input("Сколько значений вводить? "))
count = 0
sp1 = []
kor1 = ()

while count < a:
    sp1.append(int(input("Введите значение: ")))
    count += 1

kor1 = sp1
print("Список пользователя", sp1)
print("Кортеж пользователя", kor1)
