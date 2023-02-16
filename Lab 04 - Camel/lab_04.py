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

    while done not True:
        print("""A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.""")

    user_choice = input("Your choice? ")

    if user_choice == 'Q':
            print("you have quit the game.")
    if user_choice == 'q':
            print("you have quit the game.")


    elif user_choice == 'E':
        print("Travelled " + str(miles_traveled) + " miles.")
        print("You have " + str(drinks) + " drinks left")
        print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you")

    elif user_choice == 'e':
        print("Travelled " + str(miles_traveled) + " miles.")
        print("You have " + str(drinks) + " drinks left")
        print("The natives are " + str(miles_traveled - native_travel_distance) + " miles behind you")

    elif user_choice == "D":
        print("Time to rest for the night")
        print("\U0001F42A is happy and rested")


main()
