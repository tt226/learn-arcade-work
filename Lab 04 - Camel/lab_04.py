import random


def main():
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert
The natives want their camel back and are chasing you down! Survive your 
desert trek and out run the natives.\n""")

    #  variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_travel_distance = -20
    drinks = 3

    while not done:
        print("""\nA. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.\n""")

        user_choice = input("Your choice? ")

        # option Q - quit the game

        if user_choice == 'Q':
            print("you have quit the game.")
            done = True

        if user_choice == 'q':
            print("you have quit the game.")
            done = True

        # option E - user status check

        elif user_choice == 'E':
            print("\nTravelled " + str(miles_traveled) + " miles.")
            print("You have " + str(drinks) + " drinks left.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == 'e':
            print("\nYou have now travelled " + str(miles_traveled) + " miles.")
            print("You have " + str(drinks) + " drinks left.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        # option D - stopping for the night

        elif user_choice == "D":
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            camel_tiredness = 0
            print("\nTime to rest for the night.")
            print("\U0001F42A is happy and rested.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "d":
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            camel_tiredness = 0
            print("\nTime to rest for the night.")
            print("\U0001F42A is happy and rested.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        # option C - Full power mode on

        elif user_choice == "C":
            miles_traveled = miles_traveled + random.randrange(10, 21)
            thirst += 1
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            print("\U0001F42A\U0001F4A5")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "c":
            miles_traveled = miles_traveled + random.randrange(10, 21)
            thirst += 1
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            print("\U0001F42A\U0001F4A5")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        # option B - Moderate speed ahead

        elif user_choice == "B":
            miles_traveled = miles_traveled + random.randrange(5, 13)
            thirst += 1
            camel_tiredness += 1
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            print("(๑˃ᴗ˂)ﻭ")
            print("You've travelled " + str(miles_traveled) + ' miles.')
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "b":
            miles_traveled = miles_traveled + random.randrange(5, 13)
            thirst += 1
            camel_tiredness += 1
            native_travel_distance = native_travel_distance + random.randrange(7, 15)
            print("(๑˃ᴗ˂)ﻭ")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        # option A - Drinks from the canteen

        elif user_choice == "A":
            if drinks > 0:
                thirst = 0
                drinks -= 1
                print("╰( ^o^)╮╰( ^o^)╮")
                print("refreshing\n")
            else:
                print("no more water left \U0001F494\n")

        elif user_choice == "a":
            if drinks > 0:
                thirst = 0
                drinks -= 1
                print("╰( ^o^)╮╰( ^o^)╮")
                print("refreshing\n")
            else:
                print("no more water left \U0001F494\n")

        # how tired the camel is

        if camel_tiredness > 8:
            print("Your camel is dead ( ╥ω╥ )")
            print("\nGame Over")
            done = True

        elif camel_tiredness > 5:
            print("Your camel is getting tired!")

        # dying of thirst

        if thirst > 6:
            print("\nYou died of thirst!”")
            print("¯\_(ツ)_/¯")
            print("\n Game Over")
            done = True

        elif thirst > 4:
            print("You are thirsty!!! o(>< )o")

        # the native chase distance

        if native_travel_distance == miles_traveled:
            print("The natives caught you")
            print("Game Over")

        elif native_travel_distance >= miles_traveled - 15:
            print("The natives are getting closer")

        # going over or equal to 200 miles

        if miles_traveled >= 200:
            print("You Won \U0001F389")
            done = True

        # finding an oasis
        if not done and thirst < 4:
            oasis = random.randrange(1, 21)
        if oasis == 20:
            camel_tiredness = 0
            thirst = 0
            drinks = 3
            print("You found an oasis!")


main()
