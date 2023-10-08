kor1 = ((1, 2, 3), 8)
kor2 = ((1, 8, 3, 4, 8, 8, 9, 2), 8)
kor3 = ((1, 2, 8, 5, 1, 2, 9), 8)


def now(a, b):
    po = b in a
    spis = []
    cout = False
    if po == False:
        ror = ()
        return ror

    for i in a:
        if i == b and cout == True:
            spis.append(i)
            break
        if i == b:
            cout = True
        if cout == True:
            spis.append(i)

    return tuple(spis)


print(now(kor1[0], kor1[1]))
print(now(kor2[0], kor2[1]))
print(now(kor3[0], kor3[1]))
