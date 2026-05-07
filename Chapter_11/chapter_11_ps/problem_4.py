# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

# 2. Create a class "Pets' from a class "Animals' and further create a class 'Dog' from
# 'Pets'. Add a method 'bark' to class "Dog'.

# 3. Create a class "Employee' and add salary and increment properties to it.

# Write a method 'salaryAfterincrement" method with a @property decorator with a setter
# which changes the value of increment based on the salary.

# 4. Write a class 'Complex' to represent complex numbers, along with overloaded
# operators '+' and '*' which adds and multiplies them.

# 5. Write a class vector representing a vector of n dimensions. Overtoad the + and *
# operator which calculates the sum and the dot(.) product of them.

# 6. Write_str_() method to print the vector as follows:

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self,c2):
        real_part = self.r*c2.r - self.i * c2.i
        imag_part = self.r*c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1= Complex(1, 2)
c2 = Complex(3, 4)
print(c1+c2)
print(c1*c2)