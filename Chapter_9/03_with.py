f = open("fie.txt")

print(f.read())

f.close()

# instead of writing the above code we can use with with statement

with open("fie.txt") as f:
    print(f.read())

#here with statement will automatically close the file after the block of code is executed, even if an error occurs.