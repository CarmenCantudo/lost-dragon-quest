import time
import colorama  # import for font colour
from colorama import Fore

# Variables
DRAGONS_NAME = "Ignit"
weapons = ["Shield", "Golden Sword", "Axe", "Bow & Arrow", "Potion", "Cloak"] # noqa
backpack = []


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
    print(f"{DRAGONS_NAME} was born. From that day until now, we raised {DRAGONS_NAME} as kin.") # noqa
    time.sleep(3)
    print("That was until Lord Orcus, the evil warlock, took her.")# noqa
    time.sleep(3)
    print("Legend tells that on the blood moon, the blood of a blue back dragon can complete the spell to control all living creatures on planet Apollo.") # noqa
    time.sleep(3)
    print(f"It is but two days before the blood moon, and I must find and save {DRAGONS_NAME} and all those on Apollo.") # noqa
    time.sleep(3)
    print(f"But all I have is my compass made from the stone of Bolcán, pointing to {DRAGONS_NAME} and courage to guide me on this perilous quest.") # noqa
    time.sleep(3)

    continue_game = input("Will you go to save your dragon now? (Y/N): \n")
    if startGame == "n" or startGame == "N":
        print(F"Don't wait for too long, {DRAGONS_NAME} needs you!")
    elif continue_game == "y" or startGame == "Y":
        dark_forest()


def dark_forest():
    """
    First quest path
    """
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
    # Option: continue or not on the main road
    if main_road == "y" or main_road == "Y":
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
    save_man = input("Do you want to save the man? (Y/N): \n")

    # Option: save the man or continue
    if save_man == "n" or save_man == "N":
        print("You leave the camp, walking through the forest, when suddenly you hear a crack.") # noqa
        time.sleep(3)
        print("You fall through a hole in the ground and find yourself surronded by goblins.") # noqa
        game_over()
    elif save_man == "y" or save_man == "Y":
        print("You decide to save the man.")

    # Save the man
    print("You realised that there is only one goblin standing guard watching over the prisoner.") # noqa
    time.sleep(3)
    print("You won't have much time to save him before the rest of the goblins come back.") # noqa
    time.sleep(3)
    print("You decide to take some stones and throw them in the other direction so that the goblin goes to see what is happening.") # noqa
    time.sleep(3)
    print("When the goblin goes to the noise, you run around the camp to open the cage with your blacksmith tools.") # noqa
    time.sleep(3)
    print("On the way out you see some weapons but only have time to take one with you.") # noqa
    time.sleep(3)
    print("You don't have anything fight, only your blacksmith tools so you need to choose carefully but quickly before they find you.") # noqa
    time.sleep(3)
    print("The weapons are:")
    for i, weapon in enumerate(weapons):
        print(i, weapon)
    weapon_id = input("Which weapon will you choose? (Select a number)\n")
    get_weapon = weapons[weapon_id]
    time.sleep(1)
    chosen_weapon(get_weapon)


def chosen_weapon(get_weapon):
    """
    Take weapon from weapons list and move it to backpack list
    """
    if get_weapon == "shield" or get_weapon == "Shield":
        backpack.insert(0, weapons.pop(weapons.index("Shield")))
        
    elif get_weapon == "golden sword" or get_weapon == "Golden Sword":
        backpack.insert(0, weapons.pop(weapons.index("Golden Sword")))
    elif get_weapon == "axe" or get_weapon == "Axe":
        backpack.insert(0, weapons.pop(weapons.index("Axe")))
    elif get_weapon == "bow & arrow" or get_weapon == "Bow & Arrow":
        backpack.insert(0, weapons.pop(weapons.index("Bow & Arrow")))
    elif get_weapon == "potion" or get_weapon == "Potion":
        backpack.insert(0, weapons.pop(weapons.index("Potion")))
    elif get_weapon == "cloak" or get_weapon == "Cloak":
        backpack.insert(0, weapons.pop(weapons.index("Cloak")))
    else:
        print(Fore.RED + "Sorry invalid entry.")
        input_req("Please select a weapon.")


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