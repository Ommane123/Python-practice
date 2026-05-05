class Employees:
    a = 1

    @classmethod                                # class method decorator : helps access cls class attribute instead of instance attribute
    def show(cls):
        print(f"The class attribute of 'a' is {cls.a}")

e = Employees()
e.a = 45

e.show()