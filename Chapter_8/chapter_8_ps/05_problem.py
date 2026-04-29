#write a python function to remove a given word from a list and strip it at the same time

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["om", "ommane", "jumbo", "ayush"]

print(remove(l, "om"))