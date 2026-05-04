# 1. Create a Class "Programmer" for storing information of few programmers
# working at Microsoft.
# 2. Write a class "calculator" capable of finding square, cube and square root of a
# number.
# 3. Create a class with a class attribute a; create an object from it and set 'a'
# directly using object.a = o. Does this change the class attribute?
# 4. Add a static method in problem 2, to greet the user with hello.
# 5. Write a class Train which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
# 6. Can you change the self-parameter inside a class to something else (say
# "harry"). Try changing self to "slf" or "harry" and see the effects.

class programmers:
    company = "Microsoft"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p = programmers("Om", 20, 100000)
print(p.name, p.age, p.salary, p.company)

r = programmers("Rahul", 25, 150000)
print(r.name, r.age, r.salary, r.company)
  