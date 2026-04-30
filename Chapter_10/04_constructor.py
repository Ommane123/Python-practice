class Employee:
    language = "Python"     # class attribute
    salary = 100000

    def __init__(self, name, salary, language):         # dunder method or constructor which is automatically called when we create an object of the class
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object of Employee class")
    
    def getInfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")

    @staticmethod               # static method does not take self as parameter 
    def greet():
        print("Hello")

Om = Employee("Om", 100, "C++")        # we can pass any number of arguments to the constructor but it will not be used as we have not defined any parameters in the constructor
# Om.name = "Om"              # instance attribute
print(Om.name, Om.salary, Om.language)  