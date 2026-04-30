class Employee:
    language = "Python"     # class attribute
    salary = 100000

    def getInfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")

    # def greet(self):        # need to pass self as parameter
    #     print("Hello")

    @staticmethod               # static method does not take self as parameter 
    def greet():
        print("Hello")

Om = Employee()
Om.language = "Java"        # instance attribute
print(Om.language, Om.salary)          # Java 100000
print(Employee.language, Employee.salary)    # Python 100000

Om.greet()
Om.getInfo()   