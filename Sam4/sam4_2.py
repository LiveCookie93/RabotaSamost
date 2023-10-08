import random


def Kub():
    while True:
        a = random.randint(1, 6)
        if a >= 5:
            print("Вы победили! Ваше число: ", a)
            break

        elif a <= 4 and a >= 3:
            print("Кубик перебрасывается! Ваше число: ", a)
            continue

        else:
            print("Вы проиграли! Ваше число: ", a)
            break


Kub()
