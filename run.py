import time


# Variables
dragons_name = "Ignit"

def start_quest():
    """
    Story intro
    """
    print("It was five years ago when, with the shake of the earth upon the eclipse, fire filled the sky.")
    time.sleep(3)
    print("Mount Bolcán had erupted after 1000 years of sleeping.")
    time.sleep(2)
    print("They call her the dragon's láir, for when she wakes, the legend says so to a blue back dragon is born.")
    time.sleep(3)
    print("With a glimmer of light left from the moon and the fire in the sky, an oval-shaped sphere with a bright red shell began to appear.")
    time.sleep(3)
    print("Tumbling down the mountain until reaching my feet, not a crack nor a scratch to be seen.")
    time.sleep(3)
    print("Grabbing this egg to shelter in the warmth until that magical seventh night, when, with a crackle quieter than a mouse, I awoke.")
    time.sleep(3)
    print(f"{dragons_name} was born. From that day until now, we raised {dragons_name} as kin.")
    time.sleep(3)
    print("That was until Lord Orcus, the evil warlock, took her.")
    time.sleep(3)
    print("Legend tells that on the blood moon, the blood of a blue back dragon can complete the spell to control all living creatures on planet Apollo.")
    time.sleep(3)
    print(f"It is but two days before the blood moon, and I must find and save {dragons_name} and all those on Apollo.")
    time.sleep(3)
    print(f"But all I have is my compass made from the stone of Bolcán, pointing to {dragons_name} and courage to guide me on this perilous quest.")
    time.sleep(3)
    
    print("")



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
print("Welcome to the Lost Dragon's Quest!")
time.sleep(0.2)
your_name = input("What is your name? \n")
time.sleep(0.2)
print(f"Hello {your_name}!")
print()
time.sleep(0.2)
startGame = input("Are you ready for an adventure? (Y/N): \n")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
elif startGame == "y" or startGame == "Y":
    start_quest()