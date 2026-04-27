friends = ["Apple", "Orange", 5, 515.54, False, "OM"]

print(friends)
print(friends[0])

friends[0] = "Grapes"       # unlike strings list is mutable

print(friends[0])
print(friends[1:4])

friends.append("Kal")       # adds element at end of the list
print(friends)

l1 = [5,3,8,6,9,4,5,66]
l1.sort()                   # sorts the list
print(l1)

l1.insert(5, 76)            # insert 
l1.pop(3)
print(l1)

print(type(l1))