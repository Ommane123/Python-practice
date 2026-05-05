class Employees:
    a = 1

    @classmethod                                # class method decorator : helps access cls class attribute instead of instance attribute
    def show(cls):
        print(f"The class attribute of 'a' is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employees()
e.a = 45

e.name = "Om Mane"
print(e.fname)
e.show()