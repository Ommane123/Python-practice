class Employee:
    company = "ITC"
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "java"
    def printlanguage(self):            # , language
        # self.language = language
        print(f"out of all lang here is u'r lang: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    
    def showLanguage(self, name, language):
        self.name = name
        self.Language = language
        print(f"The name is {self.company} and he is good with {self.Language}")


a = Employee()
b = Programmer()

b.show("Om", 5165)
b.printlanguage()
b.showLanguage("Om", "java")