# Let's create a smooth introduction to the user
# time model will create delays between text
# Code assists from https://www.youtube.com/watch?v=FblABqaKz_U and w3schools.com/python/python_functions.asp
import time
# sys model will allow us to exit program if user wants to quit
import sys

guide_name = "AOI"
user_name = ""

# Function to print text with a delay
def delay_text(text, delay=.07):
    # Loop through each character from text and print it after delay
    for char in text:
        # char is character in text, delays the output
        sys.stdout.write(char)
        # Flush ensures that the output is printed
        sys.stdout.flush()
        # delay the time and print the next character
        time.sleep(delay)
# Be sure that this function is not in the for char in text loop, otherwise it will make the text vertical
    print()  

def intro():
    # global allows us to use the variable outside of the function. This is important because we want to use the user_name variable in other functions.
    global user_name
    delay_text("Welcome user!")
    delay_text("...", .7)
    delay_text("...", .7)
    delay_text("...", .7)
    delay_text("Loading program...")
    delay_text("Hello I'm " + guide_name + " guess you are here to start your adventure!")
    delay_text("Before we start, I need to know your name..")
    # The user can input their name and it will be stored in the user_name variable
    user_name = input("->")
    delay_text("Welcome " + user_name + "! \n" + guide_name + ": This will be a path adventure you pick a path and we will see the outcome!")

# Creating a function for user path decision making village path or explore deeper in cave path
def village_path():
    delay_text("*You exit out the cave and head towards the distance light, as you get closer you see a village. You enter the village and ask for some help.*\n*They let you sleep in a cabin for the night.*\n")
    delay_text(guide_name + ": Hey wake up " + user_name + " I can hear some noise outside, it sounds like someone is in trouble! Do you want to go check it out?")
    # The user can choose to go check it out or stay in the cabin
    choice = input("1. yes or 2. no: ")
    if choice == "1":
        delay_text("*You dash outside finding a women being tormented by a group of bandits, you notice a steel sword on the ground, you pick it up and fight off the bandits*\n")
        delay_text(guide_name + ": It was a good choice for me to pick you. Hidden potential was inside you all along, you just needed to find it. You are a true hero now! Congrats on completing the adventure!")
    elif choice == "2":
        delay_text("*You hear the cries for help getting louder and louder, then suddenly stop. A sharp axe prices through the door than a bandit enters seeing you hiding in the corner, he swings his axe at you and you are killed instantly. Better luck next time!")
        delay_text(guide_name + ": I guess you weren't ready to be a hero yet, maybe next time you will be more brave and courageous!")
        delay_text("\nAchievment Unlocked: Cowardly Adventurer")
    else:
        delay_text("Invalid choice, please choose either 1 or 2.")
        village_path()

# cave path root
def cave_path():
    delay_text(guide_name + ": Ahh I appears you want to see what is within this cave, well be careful, it could be dangerous. \n*You travel deeper into the cave and see a chest in the distance, you walk towards it and open it*\n*Inside you find a sword and a shield, you take them and continue to explore the cave*\n")
    delay_text(guide_name + ": Oh wow it looks like you found some useful items, though I wonder if you can even use them with your weak arms.. I mean I think you got this!!!\n")
    delay_text("*You ingore your guide though you are disappoint of it's remarks, you continue but, soon find yourself in a empty room, suddenly the door behind you slams shut!*\n")
    delay_text(guide_name + ": HMMM it appears that we are stuck in he- *before the guide can finish it's sentence, a slim monster appears in front of you*")
    delay_text(guide_name + ": Hey " + user_name + " it looks like we have a choice. Either we FIGHT the monster or DO NOTHING and hope it doesn't attack us.")
    # The user can choose to fight the monster or do nothing
    choice = input("\nWhat do you choose? (1.fight or 2.nothing)")
    if choice == "1":
        delay_text("*You decide to fight the monster, you lift up your sword and shield and prepare for battle. \nThe monster lunges at you but you block it with your shield, you strike back with your sword and defeat the monster!*\n")
        delay_text(guide_name + ": Wow " + user_name + " now you can say that armor isn't for show. Looks like it dropped a key, maybe it'll open that door.")
        delay_text("*You pick up the key and open the door, you find a treasure chest inside, you open it and find a lot of gold and jewels!*\n")
        delay_text(guide_name + ": Wow " + user_name + " you are rich now! I guess you can say that you are a true adventurer now! Congrats on completing the adventure!")
    elif choice == "2":
        delay_text(guide_name + ": Umm " + user_name + " it CAN SEE YOU!! *The slim monster jumps at you turning you to a puddle of goo, you have died!* Better luck next time!")
    else:
        delay_text("Invalid choice, please choose either 1 or 2.")
        cave_path()
def story():
    delay_text(guide_name + ": Now that we got the introduction out the way, you have two paths to choose from. "
    "\nPath 1: You see a light in the distance, it looks like a village. You can head towards it and see if you can find help.\n"
    "Path 2: You see a dark cave, it looks like it could be dangerous but there might be something valuable inside. You can head towards it and see if you can find anything useful.\n")
    choice = input("Which path do you choose? (1 or 2) ")
    if choice == "1":
        # If the user chooses path 1, call the village_path function
        village_path()
        
    elif choice == "2":
        # If the user chooses path 2, call the cave_path function
        cave_path()
    else:
        # If the user enters an invalid choice, print an error message and call the story function again
        delay_text("Invalid choice, please choose either 1 or 2.")
        story()

# Call the funciton to start the program
intro()
story()