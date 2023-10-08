class Student:
    def __init__(self, first, last, age, major):
        self.first = first
        self.last = last
        self.age = age
        self.major = major

    def profile(self):
        print(f"name {self.first + ' ' + self.last}")
        print(f"age: {self.age}")
        print(f"Major: {self.major}")


s = Student('Sally', 'Harris', 20, 'Biology')

class Direc(Student):
    def ruc(self):
        print("Директор организации")

d = Direc('Mas', 'Turs', 29, 'Economic')
s.profile()
d.ruc()
d.profile()