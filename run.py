import time
import os
import sys


# Variables
DRAGONS_NAME = "Ignis"
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
LEVEL_ONE = """
#######################
| YOUR JOURNEY STARTS |
|       LEVEL 1       |
#######################
"""
LEVEL_TWO = """
######################
|  THE ICE MOUNTAIN  |
|       LEVEL 2      |
######################
"""
LEVEL_THREE_CAVE = """
#####################
|  THE WINDY CAVES  |
|      LEVEL 3      |
#####################
"""
LEVEL_THREE_RIVER = """
#######################
|   THE WHITE RIVER   |
|       LEVEL 3       |
#######################
"""
FINAL_LEVEL = """
############################
|   THE WARLOCK'S CASTLE   |
|       FINAL LEVEL        |
############################
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


def game_over():
    """
    Finish the game
    """
    you_lose = """
     __   __            _                _ 
     \ \ / /__  _   _  | | ___  ___  ___| |
      \ V / _ \| | | | | |/ _ \/ __|/ _ \ |
       | | (_) | |_| | | | (_) \__ \  __/_|
       |_|\___/ \__,_| |_|\___/|___/\___(_)

    """
    print(you_lose)
    play_again = input_printing("Do you want to play again? Y/N\n")
    while True:
        if play_again.lower() == "y":
            start_quest()
            break
        elif play_again.lower() == "n":
            printing("Ok, see you soon!")
            clear_screen()
            break
        else:
            play_again = input_printing("Wrong answer. Insert Y or N.")


def win_game():
    """
    Win the quest
    """
    you_win = """
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝

    """
    print()
    print(you_win)
    print()


def warlocks_castle():
    """
    Final quest path, last level
    """
    print()
    print(FINAL_LEVEL)
    print()
    time.sleep(1)
    printing("The castle with walls higher than cliffs and a door solid iron, "
             "unbreakable.\n")
    printing("I need to find a way in without being discovered.\n")
    printing("But a weakness, the sewer appears large enough to fit a dragon "
             "and his rescuer.\n")
    use_cloak = input_printing("Should I use the invisibility cloak to enter "
                               "the sewer? Y/N")
    while True:
        if use_cloak.lower() == "n":
            printing("Suddenly, I hear footsteps behind me.\n")
            printing("I try to hide but it's too late.\n")
            printing("Some soldiers discover me and catch me.")
            game_over()
            break
        elif use_cloak.lower() == "y":
            printing("With the help of the compass, navigating the labyrinth, "
                     "the dungeons appear and so to the blue-back dragon..\n")
            break
        else:
            use_cloak = input_printing("Select Y or N.\n")
    printing("With no sound emerging from the door, I slowly open it to find "
             "my friend.\n")
    time.sleep(1)
    printing(f"Decloaking myself, {DRAGONS_NAME}, as excited as can be, runs "
             "to me, knocking everything along the path.\n")
    printing("Lord Orcus knows I am here.\n")
    printing("With no choice I must face this final challenge.")
    time.sleep(1)
    printing("I take my backpack and get the weapons.\n")
    printing("He walks into the dungeons and raises his hands to cast a spell "
             "on me.\n")
    printing("I take the shield and cover myself with it.\n")
    printing("The spell bounces off my shield and goes straight to Lord Orcus,"
             " turning him into a toad.\n")
    printing("I run to release my dragon and get out of that hideous castle.\n")  # noqa
    printing("It's time to go home.\n")
    time.sleep(1)
    win_game()


def white_river():
    """
    Third quest path, level 3
    """
    print()
    print(LEVEL_THREE_RIVER)
    print()
    time.sleep(1)
    printing("As I approach the river the sounds of nature all but disappear.\n")  # noqa
    printing("Now just rapid water fills my ears.\n")
    printing("Crossing the wooden bridge broken and soaked I hear the scream "
             "of Hydra.\n")
    printing("There she is in all her glory moving through the water like a "
             "knife through butter, ready to attack.\n")
    time.sleep(1)
    printing("You look through your backpack and see an ice bomb and a golden "
             "sword.\n")
    use_weapons = input_printing("Should I use them? Y/N")
    while True:
        if use_weapons.lower() == "n":
            printing("The Hydra is faster than me.\n")
            printing("It only takes her a few steps to capture me.\n")
            game_over()
            break
        elif use_weapons.lower() == "y":
            printing("I take the ice bomb and through it to the river.\n")
            break
        else:
            use_weapons = input_printing("Choose Y/N.\n")
    printing("It immediately turns to ice, trapping the Hydra.\n")
    printing("Unable to move she tries to reach me with her heads but she "
             "can't.\n")
    printing("I pick up the sword and start fighting the Hydra.\n")
    printing("She is stronger than me but the golden sword can hurt her and "
             "she can't grow more heads.\n")
    printing("I manage to get to her and stab her with the sword.\n")
    printing("The Hydra falls badly injured to one side and I take the "
             "opportunity to cross the river and flee.\n")
    printing(f"Finally with one last mission {DRAGONS_NAME} shall be free.\n")
    time.sleep(1)
    warlocks_castle()


def windy_cave():
    """
    Third quest path, level 3
    """
    print()
    print(LEVEL_THREE_CAVE)
    print()
    time.sleep(1)
    printing("I can see the mist coming out of the Windy Caves.\n")
    printing("As I travel further and further in the windy caves the light "
             "begins to disappear until the darkness has consumed the bright.\n")  # noqa
    printing("A loud growl of what sounds like a troll echos in the chamber of"
             " black.\n")
    printing("There is a golden sword in my backpack. The sword is flammable.\n")  # noqa
    use_sword = input_printing("Do you want to use the golden sword to light "
                               "the room? Y/N\n")
    while True:
        if use_sword.lower() == "y":
            printing("I take the sword and continue walking until I start "
                     "hearing some strange noises.\n")
            break
        elif use_sword.lower() == "n":
            printing("I see a light coming towards me.\n")
            printing("I try to hide but can't see anything.\n")
            printing("It's too late! I see some trolls coming to get me.\n")
            printing("I run and try to scape but there are a lot of them and "
                     "they catch me.\n")
            game_over()
            break
        else:
            use_sword = input_printing("Wrong answer! Do you want to use the "
                                       "golden sword to light the room? Y/N\n")
    printing("I keep walking along the underground corridor until I reach a "
             "cavern.\n")
    printing("Suddenly I find myself surrounded by sleepy trolls.\n")
    printing("If they don't hear or see me, maybe I have an opportunity to "
             "escape without being seen.\n")
    printing("I just remember seeing an invisibility cloak in the backpack.\n")
    use_cloak = input_printing("Should I use it? Y/N")
    while True:
        if use_cloak.lower() == "y":
            printing("I take the cloak and very quietly walk across the cavern"
                     " until I find myself save again and continue my quest.\n")  # noqa
            break
        elif use_cloak.lower() == "n":
            printing("Suddenly a troll gives a snoring sound that scares you "
                     "and makes you fall on one of them.\n")
            printing("The trolls wake up and instantly capture me.\n")
            game_over()
            break
        else:
            use_cloak = input_printing("Wrong answer. Should I use it? Y/N")
    printing(f"Finally with one last mission {DRAGONS_NAME} shall be free.\n")
    time.sleep(1)
    warlocks_castle()


def ice_montain():
    """
    Second quest path, level 2
    """
    print()
    print(LEVEL_TWO)
    print()
    time.sleep(1)
    printing("I can feel the mountain.")
    time.sleep(1)
    printing("The loud whistle of the wind makes you think of otherworldly "
             "screams emanating from its underground cavities.")
    time.sleep(1)
    printing("I start getting a terrible stench reaching up from the "
             "mountain's bowels.\n")
    printing("I need to continue walking but it starts getting harder with"
             " the ice.\n")
    printing("As I cross the mountain, like an avalanche, the abominable "
             "snowman appears.\n")
    printing("I quickly check the bag to get a weapon.\n")
    printing('The man said "Only fire will rid the beast of the ice"\n')
    printing("So, as soon as I see a fire bomb I take it and through it to the"
             " abominable snowman.\n")
    printing("The snowman doesn't move in time to get out of the way so the "
             "bomb explodes on top of him, covering him in flames.\n")
    printing("I run as fast as possible, leaving the mountain behind and "
             "continuing my journey.\n")
    printing("I check the compass and it points to the Evil Warlock's Castle.\n")  # noqa
    printing("There are two ways to get there: going across the White River "
             "or through the Windy Cave.\n")
    path = input_printing("Which path will you choose? WHITE RIVER (1) or "
                          "WINDY CAVE (2)\n")
    while True:
        if path == "1":
            printing("I choose the White River.\n")
            white_river()
            break
        elif path == "2":
            printing("I choose the Windy Cave.\n")
            windy_cave()
            break
        else:
            path = input_printing("That is not an option. Choose again! WHITE "
                                  "RIVER (1) or WINDY CAVE (2)\n")


def dark_forest():
    """
    First quest path, level 1
    """
    print()
    print(LEVEL_ONE)
    print()
    time.sleep(1)
    printing("The compass is pointing to the Dark Forest, so you start "
             "walking straight away.\n")
    printing("The light fades as you enter the forest, turning into a strange "
             "dark and quiet place, the sounds have all but vanished.\n")
    printing("The smell of animal or beast hangs in a still air, no flowers "
             "seem to help the uneasy odor.\n")
    printing("You need to decide if you want to continue walking along the "
             "main road or get out.\n")
    main_road = input_printing("Do you want to stay in the main road? (Y/N):\n"
                               )
    # Option: continue or not on the main road
    while True:
        if main_road.lower() == "y":
            printing("You continue on the main road, walking through the "
                     "forest, when suddenly you hear a crack.\n")
            time.sleep(1)
            printing("You fall through a hole in the ground and find yourself "
                     "surronded by goblins.\n")
            game_over()
            break
        elif main_road.lower() == "n":
            printing("You walk through the dark forest and you start hearing "
                     "lots of scary noises.\n")
            time.sleep(1)
            break
        else:
            main_road = input_printing("Enter Y or N\n")
    printing("You see some light nearby. The noises come from that area.\n")
    printing("It is a goblin camp.\n")
    print()
    printing("Suddenly a scream cuts the night and everything becomes quiet.\n")  # noqa
    printing("The goblins have a man bound to a tree.\n")
    save_man = input_printing("Do you want to save the man? (Y/N): \n")

    # Option: save the man or continue
    while True:
        if save_man.lower() == "n":
            printing("You leave the camp, walking through the forest, when "
                     "suddenly you hear a crack.\n")
            time.sleep(1)
            printing("You fall through a hole in the ground and find yourself "
                     "surronded by goblins.\n")
            game_over()
            break
        elif save_man.lower() == "y":
            printing("You decide to save the man.")
            time.sleep(1)
            break
        else:
            save_man = input_printing("Select Y or N")

    # Save the man
    printing("You realised that there is only one goblin standing guard "
             "watching over the prisoner.\n")
    printing("You won't have much time to save him before the rest of the "
             "goblins come back.\n")
    printing("You decide to take some stones and throw them in the other "
             "direction so that the goblin goes to see what is happening.\n")
    printing("When the goblin goes to the noise, you run around the camp to "
             "release the prisoner.\n")
    printing("The prisoner is now free.\n")
    printing("The man, thankful for his rescue offers some advice:\n")
    printing("- Only fire will rid the beast of the ice.\n")
    printing("On the way out you see some weapons and you take them with you.\n")  # noqa
    printing("You put the weapons in your backpack and run and hide far from "
             "the camp until everything seems safe.\n")
    printing("You say goodbye to the man and, once you are out of the forest, "
             "you check the compass to see where to go next.\n")
    printing("The compass is pointing to the Ice Mountain.\n")
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
    printing("It was five years ago when, with the shake of the earth upon "
             "the eclipse, fire filled the sky.\n")
    printing("Mount Bolcán had erupted after 1000 years of sleeping.\n")
    printing("They call her the dragon's láir, for when she wakes, the legend "
             "says so to a blue-back dragon is born.\n")
    printing("With a glimmer of light left from the moon and the fire in the "
             "sky, an oval-shaped sphere with a bright red shell began to "
             "appear.\n")
    printing("Tumbling down the mountain until reaching my feet, not a crack "
             "nor a scratch to be seen.\n")
    printing("Grabbing this egg to shelter in the warmth until that magical "
             "seventh night, when, with a crackle quieter than a mouse, I"
             " awoke.\n")
    print()
    printing(f"{DRAGONS_NAME}, the last blue-back dragon, was born.\n")
    printing(f"From that day until now, we raised {DRAGONS_NAME} as kin.\n")
    print()
    printing("That was until Lord Orcus, the evil warlock, took her.\n")
    time.sleep(1)
    printing("Legend tells that on the blood moon, the blood of a blue-back "
             "dragon can complete the spell to control all living creatures on"
             " planet Apollo.\n")
    printing("It is but two days before the Blood Moon, and I must find and "
             f"save {DRAGONS_NAME} and all those on Apollo.\n")
    printing(f"But all I have is my compass made from the stone of Bolcán, "
             f"pointing to {DRAGONS_NAME} and courage to guide me on this "
             "perilous quest.\n")
    print()

    continue_game = input_printing("Will you go to save your dragon now? "
                                   "(Y/N): \n")
    while True:
        if continue_game.lower() == "n":
            printing(f"Don't wait for too long, {DRAGONS_NAME} needs you!")
            time.sleep(5)
            clear_screen()
            main()
            break
        elif continue_game.lower() == "y":
            dark_forest()
            break
        else:
            continue_game = input_printing("Incorrect answer. Insert Y or N.\n")  # noqa
            time.sleep(2)


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
            break
        elif start_game.lower() == "y":
            start_quest()
            break
        else:
            start_game = input_printing("Wrong choice. Please, click Y or N.\n"
                                        )


main()
