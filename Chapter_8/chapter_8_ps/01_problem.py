def greatest_no(a,b,c):
    if(a > b and a > c):
        return print(a,"is greater")
    elif(b >a and b > c):
        return print(b,"is greater")
    else:
        return print(c,"is greater")
    
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))

greatest_no(a,b,c)