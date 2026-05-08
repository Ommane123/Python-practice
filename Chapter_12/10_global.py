a = 89                  # global variable

def fun():

    global a            # global keyword changes global variable like 'a' here
    a = 3               # local

    print(a)

fun()
print(a)

# ‘global’ keyword is used to modify the variable outside of the current scope.

