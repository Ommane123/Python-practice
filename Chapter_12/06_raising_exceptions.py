a = int((input("Enter a number: ")))
b = int((input("Enter a number: ")))

if(b == 0):
    raise ZeroDivisionError("hey our program is not ment to divide by 0")
else:
    print(f"the devision a/b is {a/b}")


# 8:32