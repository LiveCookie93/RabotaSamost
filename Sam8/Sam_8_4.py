class Student:
    def __init__(self, first, last, age, major):
        self.first = first
        self.last = last
        self.age = age
        self.major = major
        self.__inc()

    def profile(self):
        print(f"name {self.first + ' ' + self.last}")
        print(f"age: {self.age}")
        print(f"Major: {self.major}")


    def __inc(self):
        print("Проверка инкапсуляции")


s = Student('Sally', 'Harris', 20, 'Biology')



