like: list[str] = ['Pasta', 'Figs', 'Chocolate']

like.append('Pizza')

print(like)


planet: list[int] = [1, 2, 3, 4, 5, 6, 7, 7]
planet.append(22)
print(planet)

# copy

people: list[str] = ["Six", "seven", "perhaps"]
copy_people: list[str] = people.copy()

copy_people.remove('Six')
print(people)
print(copy_people)

ten: list[str] = ["nauuuuur", "tehehhehehe", 'wht']
copy_ten: list[str] = ten.copy()
copy_ten.remove("wht")
print(copy_ten)

