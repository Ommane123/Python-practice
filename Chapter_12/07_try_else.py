try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")       # code goes inside the else block only if the try block is executed properly if not the code will ignore else as well
    #Sometimes we want to run a piece of code when try was successful. 
