import time
import os
import sys


# Variables
DRAGONS_NAME = "Ignit"
backpack = []
weapons = ["Shield", "Golden Sword", "Axe", "Fire Bomb", "Potion", "Cloak"]
QUEST_TITLE = ("""

▄▄▌        .▄▄ · ▄▄▄▄▄    ·▄▄▄▄  ▄▄▄   ▄▄▄·  ▄▄ •        ▐ ▄ .▄▄ · 
██•  ▪     ▐█ ▀. •██      ██▪ ██ ▀▄ █·▐█ ▀█ ▐█ ▀ ▪▪     •█▌▐█▐█ ▀. 
██▪   ▄█▀▄ ▄▀▀▀█▄ ▐█.▪    ▐█· ▐█▌▐▀▀▄ ▄█▀▀█ ▄█ ▀█▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄
▐█▌▐▌▐█▌.▐▌▐█▄▪▐█ ▐█▌·    ██. ██ ▐█•█▌▐█ ▪▐▌▐█▄▪▐█▐█▌.▐▌██▐█▌▐█▄▪▐█
.▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀     ▀▀▀▀▀• .▀  ▀ ▀  ▀ ·▀▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀ 
                    .▄▄▄  ▄• ▄▌▄▄▄ ..▄▄ · ▄▄▄▄▄                    
                    ▐▀•▀█ █▪██▌▀▄.▀·▐█ ▀. •██                      
                    █▌·.█▌█▌▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪                    
                    ▐█▪▄█·▐█▄█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·                    
                    ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀                     
""")
DRAGON = """
        ..                    
        ++      :      =.     
      .*#:     +=.:     +     
     :%=#    =%%#%#=.  .#-    
    -%=#*  =#*%#:*%+:  *+*:   
   :%**%%: -==. =%#: .#%*+%   
   ##%*%%%*=:.+%%+--*%%#%*%+  
  -%#%%##:.=+%%+--=#%%%%%*%*  
  +%#%+=:.-=%#=+=:. .:*%#%%+  
  *%#-  .-=%#-#+ :==- -%%%%.  
  +%*-  -.*%+:=##*+%#  +%%:   
  .=    -.#%**:  .:**  =*.    
   .    -.+%%###*+%%:  .      
         -:*%%%%%%+.          
"""


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
    play_again = input_printing("Do you want to play again? Y/N")
    while True:
        if play_again.lower() == "y":
            start_quest()
            break
        elif play_again.lower() == "n":
            printing("Ok, see you soon!")
            clear_screen()
            break
        else:
            printing("Wrong answer. Insert Y or N.")


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
    time.sleep(1)
    printing("You FINALLY GET TO THE WARLOCK'S CASTLE.")
    time.sleep(1)
    printing("Find a way in without being discovered.")
    time.sleep(1)
    printing("FIND YOUR DRAGON")
    time.sleep(1)
    printing("STOP THE WARLOCK")
    time.sleep(1)
    printing("SAVE YOUR DRAGON")
    time.sleep(1)
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
    time.sleep(1)
    printing("You can HEAR THE SOUND OF THE WATER.")
    time.sleep(1)
    printing("FIND THE HYDRA")
    time.sleep(1)
    printing("KILL OR SCAPE FROM THE HYDRA")
    time.sleep(1)
    printing("GO TO THE EVIL WARLOCK'S CASTLE")
    time.sleep(1)
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
    time.sleep(1)
    printing("You can SEE THE MIST COMING OUT OF THE WINDY CAVE.")
    time.sleep(1)
    printing("FIND THE TROLLS")
    time.sleep(1)
    printing("KILL OR SCAPE FROM THE TROLLS")
    time.sleep(1)
    printing("GO TO THE EVIL WARLOCK'S CASTLE")
    time.sleep(1)
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
    time.sleep(1)
    printing("You can feel the mountain.")
    time.sleep(1)
    printing("The loud whistle of the wind makes you think of otherworldly \
        screams emanating from its underground cavities.")
    time.sleep(1)
    printing("You start getting a terrible stench reaching up from the \
        mountain's bowels.")
    time.sleep(1)
    printing("You need to continue walking ")
    time.sleep(1)
    printing("GET TO THE ABOMINABLE SNOWMAN")
    time.sleep(1)
    if backpack == "Fire Bomb":
        printing("USE THE Fire Bomb TO KILL IT")
    else:
        printing("TRY KILLING IT WITH THE" + ", ".join(backpack).lower())
    
    time.sleep(1)
    printing("LEAVE THE MOUNTAIN AND CONTINUE YOUR JOURNEY")
    printing("YOU CHECK THE COMPASS AND IT POINTS TO THE EVIL WARLOCK CASTLE")
    printing("THERE ARE TWO WAYS TO GET THERE: GOING ACROSS THE WHITE RIVER \
        OR THROUGH THE WINDY CAVE")
    while True:
        path = input_printing("WHICH PATH WILL YOU CHOOSE? WHITE RIVER (1) or \
            WINDY CAVE (2)")
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
    time.sleep(1)
    printing("The compass is pointing to the Dark Forest, so you start \
        walking straight away.")
    time.sleep(1)
    printing("The light fades as you enter the forest, turning into a strange \
        dark and quiet place, the sounds have all but vanished.")
    time.sleep(1)
    printing("The smell of animal or beast hangs in a still air, no flowers \
        seem to help the uneasy odor.")
    time.sleep(1)
    printing("You need to decide if you want to continue walking along the \
        main road or get out.")
    main_road = input_printing("Do you want to stay in the main road? (Y/N): \
        \n")
    # Option: continue or not on the main road
    if main_road == "y" or main_road == "Y":
        printing("You continue on the main road, walking through the forest, \
            when suddenly you hear a crack.")
        time.sleep(1)
        printing("You fall through a hole in the ground and find yourself \
            surronded by goblins.")
        game_over()
    elif main_road == "n" or main_road == "N":
        printing("You walk through the dark forest and you start hearing lots \
            of scary noises.")
        time.sleep(1)
   
    printing("You see some light nearby. The noises come from that area.")
    time.sleep(1)
    printing("It is a goblin camp.")
    time.sleep(1)
    print()
    printing("Suddenly a scream cuts the night and everything becomes quiet.")
    time.sleep(1)
    printing("The goblins have a man bound to a tree.")
    save_man = input_printing("Do you want to save the man? (Y/N): \n")

    # Option: save the man or continue
    if save_man == "n" or save_man == "N":
        printing("You leave the camp, walking through the forest, when \
            suddenly you hear a crack.")
        time.sleep(1)
        printing("You fall through a hole in the ground and find yourself \
            surronded by goblins.")
        game_over()
    elif save_man == "y" or save_man == "Y":
        printing("You decide to save the man.")
        time.sleep(1)

    # Save the man
    printing("You realised that there is only one goblin standing guard \
        watching over the prisoner.")
    time.sleep(1)
    printing("You won't have much time to save him before the rest of the \
        goblins come back.")
    time.sleep(1)
    printing("You decide to take some stones and throw them in the other \
        direction so that the goblin goes to see what is happening.")
    time.sleep(1)
    printing("When the goblin goes to the noise, you run around the camp to \
        release the prisoner.")
    time.sleep(1)
    printing("The prisoner is now free.")
    time.sleep(1)
    printing("The man, thankful for his rescue offers some advice:")
    time.sleep(1)
    printing("- Only fire will rid the beast of the ice.")
    time.sleep(1)
    printing("On the way out you see some weapons but only have time to take \
        one with you.")
    time.sleep(1)
    printing("You don't have anything to fight so you need to choose carefully\
         but quickly before they find you.")
    time.sleep(1)
    
    # Choose weapon
    new_weapon = select_weapon()
    time.sleep(1)
    printing(f"You take the {new_weapon.lower()} and run and hide far from the\
         camp until everything seems safe.")
    time.sleep(1)
    printing("You say goodbye to the man and, once you are out of the forest, \
        you check the compass to see where to go next.")
    time.sleep(1)
    printing("The compass is pointing to the Ice Mountain.")
    time.sleep(1)
    ice_montain()


def start_quest():
    """
    Story intro
    """
    time.sleep(1)
    print(DRAGON)
    print()
    time.sleep(1)
    printing("It was five years ago when, with the shake of the earth upon \
        the eclipse, fire filled the sky.\n")
    time.sleep(1)
    printing("Mount Bolcán had erupted after 1000 years of sleeping.\n")
    time.sleep(1)
    printing("They call her the dragon's láir, for when she wakes, the legend \
        says so to a blue-back dragon is born.\n")
    time.sleep(1)
    printing("With a glimmer of light left from the moon and the fire in the \
        sky, an oval-shaped sphere with a bright red shell began to appear.\n")
    time.sleep(1)
    printing("Tumbling down the mountain until reaching my feet, not a crack \
        nor a scratch to be seen.\n")
    time.sleep(1)
    printing("Grabbing this egg to shelter in the warmth until that magical \
        seventh night, when, with a crackle quieter than a mouse, I awoke.\n")
    time.sleep(1)
    printing(f"{DRAGONS_NAME} was born. From that day until now, we raised \
        {DRAGONS_NAME} as kin.")
    time.sleep(1)
    print()
    printing("That was until Lord Orcus, the evil warlock, took her.\n")
    time.sleep(1)
    printing("Legend tells that on the blood moon, the blood of a blue-back \
        dragon can complete the spell to control all living creatures on \
            planet Apollo.\n")
    time.sleep(1)
    printing(f"It is but two days before the Blood Moon, and I must find and \
        save {DRAGONS_NAME} and all those on Apollo.")
    time.sleep(1)
    printing(f"But all I have is my compass made from the stone of Bolcán, \
        pointing to {DRAGONS_NAME} and courage to guide me on this perilous \
            quest.")
    time.sleep(1)
    print()

    continue_game = input_printing("Will you go to save your dragon now? \
        (Y/N): \n")
    while True:
        if continue_game.lower() == "n":
            printing(f"Don't wait for too long, {DRAGONS_NAME} needs you!")
            clear_screen()
            time.sleep(2)
            main()
        elif continue_game.lower() == "y":
            dark_forest()
        else:
            printing("Incorrect answer. Insert Y or N.\n")


def main():
    """
    Runs the application and shows game intro
    """
    print()
    print()
    print(QUEST_TITLE)
    print()
    print()
    printing("Welcome to the Lost Dragon's Quest! \n")
    time.sleep(0.2)
    print()
    your_name = input_printing("What is your name? \n")
    time.sleep(0.2)
    print()
    printing(f"Hello {your_name}!")
    print()
    time.sleep(0.2)
    start_game = input_printing("Are you ready for an adventure? (Y/N): \n")
    while True:
        if start_game.lower() == "n":
            printing("Maybe next time!\n")
            time.sleep(3)
            clear_screen()
            main()
        elif start_game.lower() == "y":
            start_quest()
        else:
            input_printing("Wrong choice. Please, click Y or N.\n")


main()
