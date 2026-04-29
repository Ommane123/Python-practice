def multiplication_table(n):
    a = 1
    while(a <= 10):
        print(f"{n} X {a} = {n * a}")
        a += 1

n = int(input("enter number: ")) 
multiplication_table(n)