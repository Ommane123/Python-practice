'''
a = "a very long string with emails"

RAM = Volatile Memory
HDD = Non-Volatile Memory

                                                   write 
Programmer --> computer program written in python <----> FILE
                                                    read


'''

f = open("fie.txt")
data = f.read()
print(data)
f.close()