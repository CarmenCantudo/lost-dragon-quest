import time


# Variables
dragons_name = "Ignit"

def start_quest():
    """
    Story intro
    """
    print("It was five years ago when, with the shake of the earth upon the eclipse, fire filled the sky.") # noqa
    time.sleep(3)
    print("Mount Bolcán had erupted after 1000 years of sleeping.")
    time.sleep(2)
    print("They call her the dragon's láir, for when she wakes, the legend says so to a blue back dragon is born.") # noqa
    time.sleep(3)
    print("With a glimmer of light left from the moon and the fire in the sky, an oval-shaped sphere with a bright red shell began to appear.") # noqa
    time.sleep(3)
    print("Tumbling down the mountain until reaching my feet, not a crack nor a scratch to be seen.") # noqa
    time.sleep(3)
    print("Grabbing this egg to shelter in the warmth until that magical seventh night, when, with a crackle quieter than a mouse, I awoke.") # noqa
    time.sleep(3)
    print(f"{dragons_name} was born. From that day until now, we raised {dragons_name} as kin.") # noqa
    time.sleep(3)
    print("That was until Lord Orcus, the evil warlock, took her.")# noqa
    time.sleep(3)
    print("Legend tells that on the blood moon, the blood of a blue back dragon can complete the spell to control all living creatures on planet Apollo.") # noqa
    time.sleep(3)
    print(f"It is but two days before the blood moon, and I must find and save {dragons_name} and all those on Apollo.") # noqa
    time.sleep(3)
    print(f"But all I have is my compass made from the stone of Bolcán, pointing to {dragons_name} and courage to guide me on this perilous quest.") # noqa
    time.sleep(3)

    continue_game = input("Will you go to save your dragon now? (Y/N): \n")
    if startGame == "n" or startGame == "N":
        print("Don't wait for too long, {dragons_name} needs you!")
    elif continue_game == "y" or startGame == "Y":
        dark_forest()

def dark_forest():
    print()
    print("  #######################")
    print("  | YOUR JOURNEY STARTS |")
    print("  #######################")
    print()
    time.sleep(3)
    print("The compass is pointing to the North, and to get there you need to go through the Dark Forest.") # noqa
    time.sleep(3)
    print("The light fades as you enter the forest, turning into a strange dark and quiet place, the sounds have all but vanished.") # noqa
    time.sleep(3)
    print("The smell of animal or beast hangs in a still air, no flowers seem to help the uneasy odor.") # noqa
    time.sleep(3)
    print("You need to decide if you want to continue walking along the main road or get out.") # noqa
    main_road = input("Do you want to stay in the main road? (Y/N): \n")
    # Pick an option
    if main_road == "y" or main_road == "N":
        print("You continue on the main road, walking through the forest, when suddenly you hear a crack.") # noqa
        time.sleep(3)
        print("You fall through a hole in the ground and find yourself surronded by goblins.") # noqa
        game_over()
    
    print("You walk through the dark forest, listening to lots of scary noises.") # noqa
    time.sleep(3)
    print("You see some light nearby. The noises come from that area.")
    time.sleep(3)
    print("It is a goblin camp. Suddenly a scream cuts the night and everything becomes quiet.") # noqa
    time.sleep(3)
    print("The goblins have a man.")

        




def game_over():
    """
    Finish the game
    """
    print("GAME OVER")




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