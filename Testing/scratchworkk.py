for i in range(2):
    print("tell me why ain't nothing but a heartache")
    print("tell me why I never wanna hear you say that i want it that wayyyy")
for bic in range(3):
    i_need_u = True
    if i_need_u:
        print("this is what dreams are made of i think lol what")

for i in range(1,10):
    print(i+1)

for lala in range(2, 12, 1):
    print(lala)

for meowy in range(5):
    print((meowy + 1) * 2)

for i in range(10, -1, -1):
    print(i)

for item in [2, 54, 3, 2,1]:
    print(item * 99)

# nesting loop

for i in range(3):
    print("a")
    for j in range (3):
     print ("b")

# very complimentment but this is how a clock works???

for hour in range (1, 13):
# 13 is never included it will always stop at 12 hehe
    for minute in range(60):
        print(hour, minute)

# keep a tunning total

total = 0
for i in range(2):
    new_number = int(input("Enter a number:"))
    total = total + new_number
print("The total is: ", total)

# um this is kinda wack but it only guess one zero per line so there's that but i tho
# when i did nine but yk it is what it is

total: int = 0
for i in range(5):
    new_number = int(input( "Enter a number: "))
    if new_number == 0:
        total += 1
print("you entered a total of", total, "zeros")

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