class Employee:
    language = "Python"     # class attribute
    salary = 100000

Om = Employee()
Om.name = "Om"              # instance attribute
print(Om.name, Om.language, Om.salary)

rohan = Employee()
rohan.name = "Rohan"        # instance attribute
print(rohan.name, rohan.language, rohan.salary)


# here name is instance attribute and language and 
# salary are class attributes
# as they directly belong to the class.