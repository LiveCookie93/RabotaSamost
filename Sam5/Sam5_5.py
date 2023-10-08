spisok = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
i = 0
while i < len(spisok):
    count = spisok.count(spisok[i])
    if count > 1:
        spisok[i] = str(spisok[i]) * count
    i += 1
print(set(spisok))