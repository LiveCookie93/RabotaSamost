chtoKupil = input("Что купил: ")
zackok = input("Цена: ")
date = input("Когда купил: ")

pokupka = chtoKupil + " " + zackok + " " + date

file = open("pokupka.txt", "a")
file.write(pokupka)
file.close()
