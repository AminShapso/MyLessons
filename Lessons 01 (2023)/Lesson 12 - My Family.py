"""
1. class person:
init = name + age
work
eat

2. subclass parent:
init = name + family + age
work = do kaki
eat = homus flafel

3. subclass child:
init = name + family + age
work = do homework
eat = eat labane

++ say hello
"""


class Person:
    @staticmethod
    def kaki():
        print("Wow eze kaki")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("I'm going to work")

    def eat(self):
        print("MMM")

    def hello(self):
        print(f"Hello my name is: {self.name} and my Age is: {self.age}")


class Parent(Person):
    def __init__(self, name, family, age):
        super().__init__(name, age)
        self.family = family

    def eat(self):
        print("homus falfel")

    def hello(self):
        super().hello()
        print("And my Family is: " + self.family)


class Child(Person):
    def __init__(self, name, family, age):
        super().__init__(name, age)
        self.family = family

    def eat(self):
        print("labane")

    def hello(self):
        print("Hello my name is: " + self.name + "and my Age is: " + str(self.age) + "my Family is: " + self.family)


print()
