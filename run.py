import time,os,sys


# Variables
DRAGONS_NAME = "Ignit"
backpack = []
weapons = ["Shield", "Golden Sword", "Axe", "Fire Bomb", "Potion", "Cloak"]


def printing(text):
    """
    Code taken from www.101computing.net
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
  

def input_printing(text):
    """
    Code taken from www.101computing.net
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value
  
  
def clear_screen():
    """
    Code taken from www.101computing.net
    """
    os.system("clear")


def select_weapon():
    """
    Take weapon from weapons list and move it to backpack list
    """
    while select_weapon:
        printing("The weapons are:")
        for i, item in enumerate(weapons, start=1):
            print(i, item)
        get_weapon = input_printing("Which weapon will you choose?\n")
            
        if get_weapon == "1":
            new_weapon = "Shield"
            break
        elif get_weapon == "2":
            new_weapon = "Golden Sword"
            break
        elif get_weapon == "3":
            new_weapon = "Axe"
            break
        elif get_weapon == "4":
            new_weapon = "Fire Bomb"
            break
        elif get_weapon == "5":
            new_weapon = "Potion"
            break
        elif get_weapon == "6":
            new_weapon = "Cloak"
            break
        else:
            printing("Please select a weapon.")
            select_weapon()

    # Delete weapon from weapon's list and add it to the backpack
    backpack.insert(0, weapons.pop(weapons.index(new_weapon)))
    return new_weapon


def game_over():
    """
    Finish the game
    """
    printing("GAME OVER")


def win_game():
    """
    Win the quest
    """
    print()
    print("  ############################")
    print("  |                          |")
    print("  |        YOU WIN!!!        |")
    print("  |                          |")
    print("  ############################")
    print()


def warlocks_castle():
    """
    Final quest path, last level
    """
    print()
    print("  ############################")
    print("  |   THE WARLOCK'S CASTLE   |")
    print("  |       FINAL LEVEL        |")
    print("  ############################")
    print()
    time.sleep(3)
    printing("You FINALLY GET TO THE WARLOCK'S CASTLE.")
    time.sleep(3)
    printing("Find a way in without being discovered.")
    time.sleep(3)
    printing("FIND YOUR DRAGON")
    time.sleep(3)
    printing("STOP THE WARLOCK")
    time.sleep(3)
    printing("SAVE YOUR DRAGON")
    time.sleep(3)
    printing("YOU WIN")
    win_game()


def white_river():
    """
    Third quest path, level 3
    """
    print()
    print("  #######################")
    print("  |   THE WHITE RIVER   |")
    print("  |       LEVEL 3       |")
    print("  #######################")
    print()
    time.sleep(3)
    printing("You can HEAR THE SOUND OF THE WATER.")
    time.sleep(3)
    printing("FIND THE HYDRA")
    time.sleep(3)
    printing("KILL OR SCAPE FROM THE HYDRA")
    time.sleep(3)
    printing("GO TO THE EVIL WARLOCK'S CASTLE")
    time.sleep(3)
    warlocks_castle()


def windy_cave():
    """
    Third quest path, level 3
    """
    print()
    print("  ####################")
    print("  |  THE WINDY CAVE  |")
    print("  |      LEVEL 3     |")
    print("  ####################")
    print()
    time.sleep(3)
    printing("You can SEE THE MIST COMING OUT OF THE WINDY CAVE.")
    time.sleep(3)
    printing("FIND THE TROLLS")
    time.sleep(3)
    printing("KILL OR SCAPE FROM THE TROLLS")
    time.sleep(3)
    printing("GO TO THE EVIL WARLOCK'S CASTLE")
    time.sleep(3)
    warlocks_castle()


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
    printing("You can feel the mountain.")
    time.sleep(3)
    printing("The loud whistle of the wind makes you think of otherworldly screams emanating from its underground cavities.") # noqa
    time.sleep(3)
    printing("You start getting a terrible stench reaching up from the mountain's bowels.") # noqa
    time.sleep(3)
    printing("You need to continue walking ")
    time.sleep(3)
    printing("GET TO THE ABOMINABLE SNOWMAN")
    time.sleep(3)
    if backpack == "Fire Bomb":
        printing("USE THE Fire Bomb TO KILL IT")
    else:
        printing("TRY KILLING IT WITH THE" + ", ".join(backpack).lower())
    
    time.sleep(3)
    printing("LEAVE THE MOUNTAIN AND CONTINUE YOUR JOURNEY")
    printing("YOU CHECK THE COMPASS AND IT POINTS TO THE EVIL WARLOCK CASTLE")
    printing("THERE ARE TWO WAYS TO GET THERE: GOING ACROSS THE WHITE RIVER OR THROUGH THE WINDY CAVE") # noqa
    while True:
        path = input_printing("WHICH PATH WILL YOU CHOOSE? WHITE RIVER (1) or WINDY CAVE (2)") # noqa
        if path == "1":
            printing("YOU CHOOSE THE WHITE RIVER")
            white_river()
            break
        elif path == "2":
            printing("YOU CHOOSE THE WINDY CAVE")
            windy_cave()
            break
        else:
            printing("THAT IS NOT AN OPTION. CHOOSE AGAIN!")


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
    printing("The compass is pointing to the Dark Forest, so you start walking straight away.") # noqa
    time.sleep(3)
    printing("The light fades as you enter the forest, turning into a strange dark and quiet place, the sounds have all but vanished.") # noqa
    time.sleep(3)
    printing("The smell of animal or beast hangs in a still air, no flowers seem to help the uneasy odor.") # noqa
    time.sleep(3)
    printing("You need to decide if you want to continue walking along the main road or get out.") # noqa
    main_road = input_printing("Do you want to stay in the main road? (Y/N): \n")
    # Option: continue or not on the main road
    if main_road == "y" or main_road == "Y":
        printing("You continue on the main road, walking through the forest, when suddenly you hear a crack.") # noqa
        time.sleep(3)
        printing("You fall through a hole in the ground and find yourself surronded by goblins.") # noqa
        game_over()
    elif main_road == "n" or main_road == "N":
        printing("You walk through the dark forest and you start hearing lots of scary noises.") # noqa
        time.sleep(3)
   
    printing("You see some light nearby. The noises come from that area.")
    time.sleep(3)
    printing("It is a goblin camp.")
    time.sleep(3)
    print()
    printing("Suddenly a scream cuts the night and everything becomes quiet.") # noqa
    time.sleep(3)
    printing("The goblins have a man bound to a tree.")
    save_man = input_printing("Do you want to save the man? (Y/N): \n")

    # Option: save the man or continue
    if save_man == "n" or save_man == "N":
        printing("You leave the camp, walking through the forest, when suddenly you hear a crack.") # noqa
        time.sleep(3)
        printing("You fall through a hole in the ground and find yourself surronded by goblins.") # noqa
        game_over()
    elif save_man == "y" or save_man == "Y":
        printing("You decide to save the man.")
        time.sleep(3)

    # Save the man
    printing("You realised that there is only one goblin standing guard watching over the prisoner.") # noqa
    time.sleep(3)
    printing("You won't have much time to save him before the rest of the goblins come back.") # noqa
    time.sleep(3)
    printing("You decide to take some stones and throw them in the other direction so that the goblin goes to see what is happening.") # noqa
    time.sleep(3)
    printing("When the goblin goes to the noise, you run around the camp to release the prisoner.") # noqa
    time.sleep(3)
    printing("The prisoner is now free.")
    time.sleep(3)
    printing("The man, thankful for his rescue offers some advice:")
    time.sleep(3)
    printing("- Only fire will rid the beast of the ice.")
    time.sleep(3)
    printing("On the way out you see some weapons but only have time to take one with you.") # noqa
    time.sleep(3)
    printing("You don't have anything to fight so you need to choose carefully but quickly before they find you.") # noqa
    time.sleep(3)
    
    # Choose weapon
    new_weapon = select_weapon()
    time.sleep(1)
    printing(f"You take the {new_weapon.lower()} and run and hide far from the camp until everything seems safe.") # noqa
    time.sleep(3)
    printing("You say goodbye to the man and, once you are out of the forest, you check the compass to see where to go next.") # noqa
    time.sleep(3)
    printing("The compass is pointing to the Ice Mountain.")
    time.sleep(3)
    ice_montain()


def start_quest():
    """
    Story intro
    """
    printing("It was five years ago when, with the shake of the earth upon the eclipse, fire filled the sky.") # noqa
    time.sleep(3)
    printing("Mount Bolcán had erupted after 1000 years of sleeping.")
    time.sleep(2)
    printing("They call her the dragon's láir, for when she wakes, the legend says so to a blue back dragon is born.") # noqa
    time.sleep(3)
    printing("With a glimmer of light left from the moon and the fire in the sky, an oval-shaped sphere with a bright red shell began to appear.") # noqa
    time.sleep(3)
    printing("Tumbling down the mountain until reaching my feet, not a crack nor a scratch to be seen.") # noqa
    time.sleep(3)
    printing("Grabbing this egg to shelter in the warmth until that magical seventh night, when, with a crackle quieter than a mouse, I awoke.") # noqa
    time.sleep(3)
    printing(f"{DRAGONS_NAME} was born. From that day until now, we raised {DRAGONS_NAME} as kin.") # noqa
    time.sleep(3)
    print()
    printing("That was until Lord Orcus, the evil warlock, took her.")# noqa
    time.sleep(3)
    printing("Legend tells that on the blood moon, the blood of a blue back dragon can complete the spell to control all living creatures on planet Apollo.") # noqa
    time.sleep(3)
    printing(f"It is but two days before the blood moon, and I must find and save {DRAGONS_NAME} and all those on Apollo.") # noqa
    time.sleep(3)
    printing(f"But all I have is my compass made from the stone of Bolcán, pointing to {DRAGONS_NAME} and courage to guide me on this perilous quest.") # noqa
    time.sleep(3)

    continue_game = input_printing("Will you go to save your dragon now? (Y/N): \n")
    if startGame == "n" or startGame == "N":
        printing(f"Don't wait for too long, {DRAGONS_NAME} needs you!")
    elif continue_game == "y" or startGame == "Y":
        dark_forest()


# Game intro (From Comp Sci Central: https://youtu.be/ypNFNr72Xe8)
print()
print()
print("▄▄▌        .▄▄ · ▄▄▄▄▄    ·▄▄▄▄  ▄▄▄   ▄▄▄·  ▄▄ •        ▐ ▄ .▄▄ · ")
print("██•  ▪     ▐█ ▀. •██      ██▪ ██ ▀▄ █·▐█ ▀█ ▐█ ▀ ▪▪     •█▌▐█▐█ ▀. ")
print("██▪   ▄█▀▄ ▄▀▀▀█▄ ▐█.▪    ▐█· ▐█▌▐▀▀▄ ▄█▀▀█ ▄█ ▀█▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄")
print("▐█▌▐▌▐█▌.▐▌▐█▄▪▐█ ▐█▌·    ██. ██ ▐█•█▌▐█ ▪▐▌▐█▄▪▐█▐█▌.▐▌██▐█▌▐█▄▪▐█")
print(".▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀     ▀▀▀▀▀• .▀  ▀ ▀  ▀ ·▀▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀ ")
print("                    .▄▄▄  ▄• ▄▌▄▄▄ ..▄▄ · ▄▄▄▄▄                    ")
print("                    ▐▀•▀█ █▪██▌▀▄.▀·▐█ ▀. •██                      ")
print("                    █▌·.█▌█▌▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪                    ")
print("                    ▐█▪▄█·▐█▄█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·                    ")
print("                    ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀                     ")
print()
print()
printing("Welcome to the Lost Dragon's Quest!")
time.sleep(0.2)
your_name = input_printing("What is your name? \n")
time.sleep(0.2)
printing(f"Hello {your_name}!")
print()
time.sleep(0.2)
startGame = input_printing("Are you ready for an adventure? (Y/N): \n")
if startGame == "n" or startGame == "N":
    printing("Maybe next time")
elif startGame == "y" or startGame == "Y":
    start_quest()
