class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: Woof Woof!")


d1 = Dog("Amber", 1)

d1.bark()
