total = 0
for i in range (1, 5):
    total += i
print(total)

# this added up all intergers 1 - 4


# while loop


total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)

# these two are the same thing

# while loops are usual when you don't know how many loops you need beforehand

given_list = [5, 4, 3, 2, 1, -2, -3, -5]
total12 = 0
i = 0
while given_list[i] > 0:
    total12 += given_list[i]
    i += 1

print(total12)
