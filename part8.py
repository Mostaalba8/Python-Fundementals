from random import randint
import math
# Indicating what a function returns:
def adding_int(a,b) -> int:  # by using '-> int'
    return a + b

# Calculating the square root of a number using python standard library
def square_root(n: int) -> int:
    return math.sqrt(n)


class Character:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age
        self.list_of_powers: dict = {}
        self.wallet: dict = {}

leaf_shinobi = Character(name = 'Naruto', age = '30')
leaf_shinobi.list_of_powers = {'rasengan':80, 'shadow clone':80}
leaf_shinobi.wallet = {'GBP':1023, 'USD':130, 'BTC':0.02543222}
print(leaf_shinobi.wallet)
print(leaf_shinobi.list_of_powers)
user_preference_pt3 = input('What powers would you like to add?: ')
leaf_shinobi.list_of_powers[user_preference_pt3.lower()] = randint(1, 100) if user_preference_pt3.lower() not in leaf_shinobi.list_of_powers else None
if leaf_shinobi.list_of_powers[user_preference_pt3.lower()] > 50 and  leaf_shinobi.list_of_powers[user_preference_pt3.lower()] <= 80:
    print('COOL')
elif  leaf_shinobi.list_of_powers[user_preference_pt3.lower()] > 80:
    print('SUPER COOL')
print(leaf_shinobi.list_of_powers)


