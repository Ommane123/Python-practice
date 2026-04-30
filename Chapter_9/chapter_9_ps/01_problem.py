# 1. Write a program to read the text from a given file 'poems.txt' and find out whether it
# contains the word 'twinkle'.

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in the poem")
else:
    print("Twinkle is not present in the poem")
f.close()
