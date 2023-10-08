kor1 = ((1, 2, 3), 1)
kor2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
kor3 = ((2, 4, 6, 6, 4, 2), 9)


def foo(tpl, a):
    if not (a in tpl):
        return tpl
    else:
        k = tpl.index(a)
        return tuple(list(tpl)[0:k] + list(tpl[k + 1:]))


print(foo((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
