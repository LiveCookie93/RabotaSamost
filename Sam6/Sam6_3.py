from collections import Counter


def spis(a):
    slovar = {}
    for i in a:
        slovar[i] = slovar.get(i, 0) + 1

    ty = Counter(slovar)

    high = ty.most_common(3)

    return high


a = input("Введите последовательность цифр, минимум 15: ")
if len(a) > 15:
    beta = spis(a)
    print(beta)
else:
    print("Длина строки меньше 15!")
