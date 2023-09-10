import random
import time

def print_with_delay(text, delay=0.01):
    """Prints text character by character with a delay between each character."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    while True:
        current_time = time.localtime()
        formatted_time = time.strftime("%H:%M", current_time)

        print("""
        ************************************
                 The Beach Mystery
        ************************************
        """)
        print_with_delay("\nWelcome to the Choose-Your-Own-Adventure application!")
        print_with_delay("\nYou decide what happens by making choices. ")
        print_with_delay("\nAnswer the questions to navigate through the story.")
        print_with_delay("\nEnter ' yes' or 'no' to answer the questions.")
        print_with_delay("\nEach question will provide you with your choices.")
        print_with_delay("\nExcept the first 5, which you can answer with anything!")
        time.sleep(1)
        print_with_delay("\nAfter entering your choice.")
        input("\nPress the enter key to continue...")

        # Ask the user 5 questions and store the answer in variables

        # Variable 1    
        firstName = input("\nWhat is your first name:  ")
        while len(firstName) == 0:
            firstName = input("\nWhat is your first name: ")

        # Variable 2
        favoriteColor = input("\nWhat is your favorite color:  ")
        while len(favoriteColor) == 0:
            favoriteColor = input("\nWhat is your favorite color:  ")

        # Variable 3
        favoriteAnimal = input("\nWhat is your favorite animal:  ")
        while len(favoriteAnimal) == 0:
            favoriteAnimal = input("\nWhat is your favorite animal:  ")

        # Variable 4
        cartoonChar = input("\nWho is your favorite cartoon character:  ")
        while len(cartoonChar) == 0:
            cartoonChar = input("\nWho is your favorite cartoon character:  ")

        # Variable 5
        favoriteJewel = input("\nWhat is your favorite jewel:  ")
        while len(favoriteJewel) == 0:
            favoriteJewel = input("\nWhat is your favorite jewel:  ")

        print("\nHello, {}!".format(firstName))
        time.sleep(1)
        print("It is a beautiful day on the beach.")
        print("You are walking, enjoying the sounds of the ocean & the sand beneath your toes.")
        time.sleep(1)
        print("As you are walking along, your foot bumps something hard.")
        time.sleep(1)
        print("Curious, you start digging.")
        time.sleep(1)
        print("You finally unveil what was hidden in the sand.")
        time.sleep(2)
        print_with_delay(r"""
                        ____...------------...____
                   _.-"` /o/__ ____ __ __  __ \o\_`"-._
                 .'     / /                    \ \     '.
                 |=====/o/======================\o\=====|
                 |____/_/________..____..________\_\____|
                 /   _/ \_     <_o#\__/#o_>     _/ \_   \
                 \________________\####/________________/
                  |===\!/========================\!/===|
                  |   |=|          .---.         |=|   |
                  |===|o|=========/     \========|o|===|
                  |   | |         \() ()/        | |   |
                  |===|o|======{'-.) A (.-'}=====|o|===|
                  | __/ \__     '-.\uuu/.-'    __/ \__ |
                  |         ==== .'.'^'.'.====|
                  |  _\o/   __  {.' __  '.} _   _\o/  _|
                  `""""-""""""""""""""""""""""""""-""""`
        """)

        print("\nIt's a pirate's chest!")
        time.sleep(1)
        print()
        print(f"You look at your {cartoonChar} watch to see what time it is", formatted_time)
        time.sleep(1)

        # Ask the user to make their first decision
        treasureChest = input(f"\nDo you have time to open the chest?  Type yes or no:  ")
        while treasureChest.lower() not in ['yes', 'no']:
            if treasureChest.strip() == "":
                print("You must enter 'yes' or 'no'.")
            else:
                print("Invalid response. Please type yes or no.")
            treasureChest = input("\nDo you have time to open the chest?  Type yes or no:  ")

        if treasureChest.lower() == 'yes':
            print("\nIt takes some strength but you finally pry open the lid.")
            time.sleep(1)
            print(f"Inside you find a treasure map and 1 {favoriteColor} {favoriteJewel}.")
            time.sleep(1)
            print(f"You pocket the {favoriteJewel} and study the treasure map. ")
            # Treasure Hunt Instead of Cave Exploration
            treasureHunt = input(f"\nDo you want to follow the map?  Type yes or no:  ")
            while treasureHunt.lower() not in ['yes', 'no']:
                if treasureHunt.strip() == "":
                    print("You must enter 'yes' or 'no'.")
                else:
                    print("Invalid response. Please type yes or no.")
                treasureHunt = input("\nDo you want to follow the map?  Type yes or no:  ")

            if treasureHunt.lower() == 'yes':
                print("You brave the rough seas and finally land on the island.")
                time.sleep(2)
                print(f"As you bring your boat ashore you see two men.")
                print(f"They are guarding a path through the brush.")
                time.sleep(2)

                # Present a puzzle for the user to solve
                dialogue = "Only the one with the map may pass."
                formatted_dialogue = "\033[1m" + dialogue + "\033[0m"
                print(f"One of the men says, {formatted_dialogue}")
                print("The other man speaks up:")
                time.sleep(1)
                print("I'll let you pass if you can solve this riddle:")
                time.sleep(1)
                print("I speak without a mouth and hear without ears.")
                print("I have no body, but I come alive with the wind. What am I?")
                time.sleep(1)

                riddleAnswer = input("\nEnter your answer: ")
                while riddleAnswer.lower() != 'echo':
                    print("That answer is incorrect. Please try again.")
                    riddleAnswer = input("Enter your answer: ")

                print("Correct! You may pass.")
                print("You start walking along the path through the overgrown brush.")
                time.sleep(2)
                print("The dark path leads you to a clearing with a gnarled oak tree.")
                print("A ray of sunshine beams down.")
                print(f"There, beneath the old oak tree, it's a massive pile of gold.")
                time.sleep(2)
                print("It must be your lucky day!")
                time.sleep(1)
                print(f"Beside the gold, sleeping peacefully in the sun, is a beautiful {favoriteAnimal}!")
                time.sleep(1)
            else:
                # If you open the chest but choose not to follow the map, you go to the cave
                print("You decide to continue your walk. ")
                print("As you round a curve you see a dark cave.")
                time.sleep(1)
                # Ask the user to make the second choice
                decision2 = input(f"It looks spooky, do you want to enter? Please type yes or no:  ")
                while decision2.lower() not in ['yes', 'no']:
                    if decision2.strip() == "":
                        print("You must enter 'yes' or 'no'.")
                    else:
                        print("Invalid response. Please type yes or no.")
                    decision2 = input(f"It looks spooky, do you want to enter? Please type yes or no:  ")

                if decision2.lower() == 'yes':
                    print(f"You cautiously enter....")
                    time.sleep(2)
                    print("The air is damp and smells like seaweed and mildew.")
                    time.sleep(1)
                    print("A few feet in you find yourself at a fork. ")
                    time.sleep(1)
                    print("The cave splits into a left passage and a right passage. ")
                    caveChoice = input("Which path will you take? Type 'left' or 'right': ")

                    while caveChoice.lower() not in ['left', 'right']:
                        if caveChoice.strip() == "":
                            print("You must enter 'left' or 'right'.")
                        else:
                            print("Invalid response. Please type 'left' or 'right'.")
                        caveChoice = input("Which path will you take? Type 'left' or 'right': ")

                    if caveChoice.lower() == 'left':
                        print("You venture down the left passage and after a while, you find a hidden chamber.")
                        time.sleep(1)
                        print("In the chamber, you discover a pile of glittering treasure!")
                        time.sleep(1)
                        print(f"You smile as your fingers rub the {favoriteJewel}'s smooth surface.")
                        print(f"Congratulations! You've struck it rich.")
                    else:
                        print("You choose the right passage and follow it deeper into the cave.")
                        time.sleep(1)
                        print(f"Surprisingly, you stumble upon a cozy den,")
                        time.sleep(1)
                        print(f"and there, sleeping peacefully, is a beautiful {favoriteAnimal}!")
                        time.sleep(1)
                        print("What a magical discovery!")
                else:
                    print("You decide the cave is too spooky.")
                    time.sleep(1)
                    print(f"You smile as your fingers rub the {favoriteJewel}'s smooth surface.")
                    print("It was still a good walk.")
                    time.sleep(2)
        else:
            # If you choose not to open the chest, you go to the cave
            print("You decide to continue your walk. ")
            print("As you round a curve you see a dark cave.")
            time.sleep(1)
            # Ask the user to make the second choice
            decision2 = input(f"It looks spooky, do you want to enter? Please type yes or no:  ")
            while decision2.lower() not in ['yes', 'no']:
                if decision2.strip() == "":
                    print("You must enter 'yes' or 'no'.")
                else:
                    print("Invalid response. Please type yes or no.")
                decision2 = input(f"It looks spooky, do you want to enter? Please type yes or no:  ")

            if decision2.lower() == 'yes':
                print(f"You cautiously enter....")
                time.sleep(2)
                print("The air is damp and smells like seaweed and mildew.")
                time.sleep(1)
                print("A few feet in you find yourself at a fork. ")
                time.sleep(1)
                print("The cave splits into a left passage and a right passage. ")
                caveChoice = input("Which path will you take? Type 'left' or 'right': ")

                while caveChoice.lower() not in ['left', 'right']:
                    if caveChoice.strip() == "":
                        print("You must enter 'left' or 'right'.")
                    else:
                        print("Invalid response. Please type 'left' or 'right'.")
                    caveChoice = input("Which path will you take? Type 'left' or 'right': ")

                if caveChoice.lower() == 'left':
                    print("You venture down the left passage and after a while, you find a hidden chamber.")
                    time.sleep(1)
                    print("In the chamber, you discover a pile of glittering treasure!")
                    time.sleep(1)
                    print(f"You smile as your fingers rub the {favoriteJewel}'s smooth surface.")
                    print(f"Congratulations! You've struck it rich.")
                else:
                    print("You choose the right passage and follow it deeper into the cave.")
                    time.sleep(1)
                    print(f"Surprisingly, you stumble upon a cozy den,")
                    time.sleep(1)
                    print(f"and there, sleeping peacefully, is a beautiful {favoriteAnimal}!")
                    time.sleep(1)
                    print("What a magical discovery!")
            else:
                print("You decide the cave is too spooky.")
                time.sleep(1)
                print(f"You smile as your fingers rub the {favoriteJewel}'s smooth surface.")
                print("It was still a good walk.")
                time.sleep(2)

        play_again = input("Would you like to play again? Enter 'yes' or 'no': ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
