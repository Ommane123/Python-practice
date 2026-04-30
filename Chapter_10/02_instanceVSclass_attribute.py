class Employee:
    language = "Python"     # class attribute
    salary = 100000

Om = Employee()
Om.language = "Java"        # instance attribute
print(Om.language, Om.salary)          # Java 100000
print(Employee.language, Employee.salary)    # Python 100000