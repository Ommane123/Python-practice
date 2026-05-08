# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

a = int(input("Enter a number for multiplication table: "))

# list = [1,2,3,4,5,6,7,8,9,10]

# tables = [a*i for i in list]

table = [a*i for i in range(1,11)]

print(table)