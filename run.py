# Game intro (From Comp Sci Central: https://youtu.be/ypNFNr72Xe8)

print()
print()
print("     ######################")
print("     |                    |")
print("     |   Lost Dragon's    |")
print("     |       Quest        |")
print("     |                    |")
print("     ######################")
print()
print()
print("Hello!")
your_name = input("What is your name? ")
print(f"Hello {your_name}!")
print()
startGame = input("Would you like to go on a quest? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
elif startGame == "y" or startGame == "Y":
    start_quest()