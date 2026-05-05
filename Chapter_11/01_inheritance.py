class Employee:
    company = "ITC"
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:                                                                     # instead of doing this we'll inherit
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.Language}")

class Programmer(Employee):
    company = "ITC Infotech"
    
    def showLanguage(self, name, language):
        self.name = name
        self.Language = language
        print(f"The name is {self.name} and he is good with {self.Language}")


a = Employee()
b = Programmer()

print(a.company, b.company)

b.show("Om", 5156)
b.showLanguage("Om", "Python")