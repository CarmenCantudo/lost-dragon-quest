import time
import colorama  # import for font colour
from colorama import Fore

# Variables
DRAGONS_NAME = "Ignit"
backpack = []
weapons = ["Shield", "Golden Sword", "Axe", "Fire Bomb", "Potion", "Cloak"] # noqa


def chosen_weapon(get_weapon):
    """
    Take weapon from weapons list and move it to backpack list
    """
    if get_weapon == "0":
        backpack.insert(0, weapons.pop(weapons.index("Shield")))
        ice_montain()
    elif get_weapon == "1":
        backpack.insert(0, weapons.pop(weapons.index("Golden Sword")))
        ice_montain()
    elif get_weapon == "2":
        backpack.insert(0, weapons.pop(weapons.index("Axe")))
        ice_montain()
    elif get_weapon == "3":
        backpack.insert(0, weapons.pop(weapons.index("Fire Bomb")))
        ice_montain()
    elif get_weapon == "4":
        backpack.insert(0, weapons.pop(weapons.index("Potion")))
        ice_montain()
    elif get_weapon == "5":
        backpack.insert(0, weapons.pop(weapons.index("Cloak")))
        ice_montain()


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
    print()
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
    First quest path, level 1
    """
    print()
    print("  #######################")
    print("  | YOUR JOURNEY STARTS |")
    print("  |       LEVEL 1       |")
    print("  #######################")
    print()
    time.sleep(3)
    print("The compass is pointing to the Dark Forest, so you start walking straight away.") # noqa
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
    elif main_road == "n" or main_road == "N":
        print("You walk through the dark forest and you start hearing lots of scary noises.") # noqa
        time.sleep(3)
   
    print("You see some light nearby. The noises come from that area.")
    time.sleep(3)
    print("It is a goblin camp.")
    time.sleep(3)
    print()
    print("Suddenly a scream cuts the night and everything becomes quiet.") # noqa
    time.sleep(3)
    print("The goblins have a man bound to a tree.")
    save_man = input("Do you want to save the man? (Y/N): \n")

    # Option: save the man or continue
    if save_man == "n" or save_man == "N":
        print("You leave the camp, walking through the forest, when suddenly you hear a crack.") # noqa
        time.sleep(3)
        print("You fall through a hole in the ground and find yourself surronded by goblins.") # noqa
        game_over()
    elif save_man == "y" or save_man == "Y":
        print("You decide to save the man.")
        time.sleep(3)

    # Save the man
    print("You realised that there is only one goblin standing guard watching over the prisoner.") # noqa
    time.sleep(3)
    print("You won't have much time to save him before the rest of the goblins come back.") # noqa
    time.sleep(3)
    print("You decide to take some stones and throw them in the other direction so that the goblin goes to see what is happening.") # noqa
    time.sleep(3)
    print("When the goblin goes to the noise, you run around the camp to release the prisoner.") # noqa
    time.sleep(3)
    print("The prisoner is now free.")
    time.sleep(3)
    print("The man, thankful for his rescue offers some advice:")
    time.sleep(3)
    print("- Only fire will rid the beast of the ice.")
    time.sleep(3)
    print("On the way out you see some weapons but only have time to take one with you.") # noqa
    time.sleep(3)
    print("You don't have anything to fight so you need to choose carefully but quickly before they find you.") # noqa
    time.sleep(3)
    
    # Choose weapon
    get_weapon = input("Which weapon will you choose?\n")
    chosen_weapon(get_weapon)
    time.sleep(1)
    print("You take the weapon and run and hide far from the camp until everything seems safe.") # noqa
    time.sleep(3)
    print("You take the weapon and put it in your backpack.")
    time.sleep(3)


def ice_montain():
    """
    Second quest path, level 2
    """
    print()
    print("  ######################")
    print("  |  THE ICE MOUNTAIN  |")
    print("  |       LEVEL 2      |")
    print("  ######################")
    print()
    time.sleep(3)
    print("You say goodbye to the man and, once you are out of the forest, you check the compass to see where to go next.") # noqa
    time.sleep(3)
    print("The compass is pointing to the Ice Mountain.")
    time.sleep(3)
    print("The loud whistle of the wind makes you think of otherworldly screams emanating from its underground cavities.") # noqa
    time.sleep(3)
    print("You start getting a terrible stench reaching up from the mountain's bowels.") # noqa
    time.sleep(3)
    print("You need to continue walking ")


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