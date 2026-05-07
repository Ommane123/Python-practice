class Animal:
    def __init__(self):
        print("This is a Animals Class")

class Pet(Animal):
    def __init__(self):
        print("This is a Pets Class")

class Dog(Pet):
    def __init__(self):
        super().__init__()
        print("This is a Dog Class")
    
    @staticmethod
    def bark():
        print("Dogs can bark: bow bow!")

d = Dog()

d.bark()