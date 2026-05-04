class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square_root is {self.n**0.5}")          # ** is gives us the square root of a number
        print(f"The square_root is {self.n*0.5}")           # * is gives us the half of a number

a = calculator(25)
a.square()
a.cube()
a.square_root()