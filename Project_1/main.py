import random
'''
-1 = rock
1 = paper
0 = scissors

'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
yourDict = {"r": 1, "p": -1, "s": 0}
revDict = {1:"rock", -1:"paper", 0:"scissors"}

you = yourDict[youstr]

print(f"you chose {revDict[you]}\ncomputer chose {revDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == -1):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You lose")

    else:
        print("something went wrong")