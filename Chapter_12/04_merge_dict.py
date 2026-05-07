dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 3, 'd' : 4}  #overwrites elements cause no dups

merged = dict1 | dict2
print(merged)

# o/p = {'a': 1, 'b': 3, 'd': 4}