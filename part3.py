from random import randint

# various operations that can be performed on dictionaries and their elements

x = {'England':'Europe', 'Norway':'Europe', 'Iraq':'Asia'}
print(x)

# x.keys() ------------------- will return all the keys
# x.values ------------------- will return all the values
# x['Bulgaria'] = 'Europe' --- will add an entry
# x['England'] = 'Asia' ------ will change an entry
# del x['England'] ----------- will delete an entry
# y = x.copy() --------------- will make a copy of x

# country = input()
# continent = x[country]
# print(continent)

# z = randint(1,100)
# print(z)

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_powers = {}
        self.wallet = {}






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


