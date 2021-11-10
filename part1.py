from datetime import date, datetime


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_powers = []






leaf_shinobi = Character(name = 'Naruto', age = '30')
leaf_shinobi.list_of_powers = ['Rasengan', 'Shadow Clone']
print(leaf_shinobi.list_of_powers)
user_preference = input('What powers would you like to add?')
leaf_shinobi.list_of_powers.append(user_preference) if user_preference not in leaf_shinobi.list_of_powers else None
print(leaf_shinobi.list_of_powers)

# name = "Mostafa"
# BIRTH_DATE = "8-August-1999"
# print(BIRTH_DATE)
# x = datetime.strptime(BIRTH_DATE, "%d-%B-%Y")
# print(x)
# age = date.today().year - x.year
# print(age)
# height = 180.33
# siblings = 3
# languages = ['Norwegian', 'English', 'Arabic']
# male = True

