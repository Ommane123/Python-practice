# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

a = int(input("Enter a number for multiplication table: "))

list = [a*a for a in list]

print(list)