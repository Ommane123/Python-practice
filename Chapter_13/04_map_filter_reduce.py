from functools import reduce
#Map Example

l = [1,2,3,4,5]

square = lambda x: x*x

sqlist = map(square, l)

print(list(sqlist))

#Filter Example

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)

print(list(onlyEven))

# Reduce Example

def sum(a, b):
    return a+b

print(reduce(sum, l))


'''
If the function computes sum of two numbers and the list is [1,2,3,4]

1 2 3 4
| /
3   3   4
|  /
6    4
|  __/
10

'''