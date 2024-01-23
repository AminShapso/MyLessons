class Calc:
    @staticmethod
    def add(a, b):
        return a + b


class Person():
    def speak(self):
        print("I am a Person")

    def set_age(self, age):
        self.age = age


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am an Animal")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "dog"


class Cheeta(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # Super = Animal
        self.type = "cheeta"

    def speak(self):  # This Overrides "speak" in Animal
        print("Hello I am " + str(self.name))

    def eat(self):
        print("Give me tune bitch")


list_of_animals = []
list_of_animals.append(Animal("ani", 23))
list_of_animals.append(Dog("Tim 1", 5))
list_of_animals.append(Dog("Tim 2", 5))
list_of_animals.append(Cheeta("Chichi", 1222))

for animal in list_of_animals:
    print(f"{animal.name = }")
    print(f"{animal.age = }")
    animal.speak()
    print()
