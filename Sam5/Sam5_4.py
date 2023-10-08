spisok = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]

res = []
for i in spisok:
    if i > 2:
        res.append(i)
spisok = res
print("Список без двоек:", res)

i = 0
while i < len(spisok):

    if spisok[i] == 3:
        spisok[i] = 4
    i += 1

print("Список без двоей и троек", spisok)
