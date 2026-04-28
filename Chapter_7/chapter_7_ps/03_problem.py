# take no from user if 18 underage or you can enjoy.

age = float(input("Enter your age: "))

if(age >= 18):
    print("you can enjoy")
elif(age < 0):
    print("Enter vaild age")
elif(age == 0):
    print("you are not born yet")
elif(age > 150):
    print("you are logically dead")
else:
    print("you cant enjoy")