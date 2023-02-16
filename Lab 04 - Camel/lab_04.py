import random


def main():
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert
The natives want their camel back and are chasing you down! Survive your 
desert trek and out run the natives.\n""")
    #  variable
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_travel_distance = -20
    drinks = 3

    while done == False:
        print("""\nA. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.\n""")

        user_choice = input("Your choice? ")

        if user_choice == 'Q':
            print("you have quit the game.")
            break
        if user_choice == 'q':
            print("you have quit the game.")
            break
        elif user_choice == 'E':
            print("\nTravelled " + str(miles_traveled) + " miles.")
            print("You have " + str(drinks) + " drinks left.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == 'e':
            print("\nYou have now travelled " + str(miles_traveled) + " miles.")
            print("You have " + str(drinks) + " drinks left.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "D":
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("\nTime to rest for the night.")
            print("\U0001F42A is happy and rested.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "d":
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("\nTime to rest for the night.")
            print("\U0001F42A is happy and rested.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "C":
            miles_traveled = miles_traveled + random.randrange(10, 20)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("\U0001F42A\U0001F4A5")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "c":
            miles_traveled = miles_traveled + random.randrange(10, 20)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("\U0001F42A\U0001F4A5")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "B":
            miles_traveled = miles_traveled + random.randrange(5, 12)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("(๑˃ᴗ˂)ﻭ")
            print("You've travelled " + str(miles_traveled) + ' miles.')
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "b":
            miles_traveled = miles_traveled + random.randrange(5, 12)
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            native_travel_distance = native_travel_distance + random.randrange(7, 14)
            print("(๑˃ᴗ˂)ﻭ")
            print("You've travelled " + str(miles_traveled) + " miles.")
            print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you.\n")

        elif user_choice == "A":
            if drinks > 0:
                thirst = 0
                drinks = drinks - 1
                print("╰( ^o^)╮╰( ^o^)╮")
                print("refreshing\n")
            else:
                print("no more water left \U0001F494\n")

        elif user_choice == "a":
            if drinks > 0:
                thirst = 0
                drinks = drinks - 1
                print("╰( ^o^)╮╰( ^o^)╮")
                print("refreshing\n")
            else:
                print("no more water left \U0001F494\n")

        if camel_tiredness > 8:
            print("Your camel is dead ( ╥ω╥ )")
            print("\nGame Over")
            break

        elif camel_tiredness > 5:
            print("Your camel is getting tired!")

        if thirst > 6:
            print("\nYou died of thirst!”")
            print("¯\_(ツ)_/¯")
            print("\n Game Over")
            break

        elif thirst > 4:
            print("You are thirsty!!! o(>< )o")

        if native_travel_distance == miles_traveled:
            print("The natives caught you")
            print("Game Over")

        elif native_travel_distance >= miles_traveled - 15:
            print("The natives are getting closer")

        if miles_traveled >= 199:
            print("You Won \U0001F389")
            break




main()
