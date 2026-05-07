try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print(v)
except Exception as e:
    print(e)

print("Thank u")

'''
We can also specify the exception to catch like below: 

try: 
    # Code 
except ZeroDivisionError: 
    # Code 
except TypeError: 
    # Code 
except: 
    # Code       # All other exceptions are handled here.
'''