class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name}在吃饭")
        print(f"name : {self.name}, age:{self.age}, gender: {self.gender}")

    def drink(self):
        print(f"{self.name}在喝饮料")
        print(f"name : {self.name}, age:{self.age}, gender: {self.gender}")


p3 = Person("Tom", "7", "男")
print(p3.name)
p3.eat()
p4 = Person("Jer", "6", "女")
p4.drink()

