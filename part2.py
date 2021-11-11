temp_list = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
temp_list2 = [1,2,3,4,5,6,7,8,9]


## To find the various of operations that can be done to a list
# temp_list.
#
# Sort
# Pop
# Copy
# Count
# Index
# Append
# Extend
# Clear

# temp_list.

print(temp_list2[2::2])
# list[a:b:c]
# a = starting index (default = 0)
# b = last index (default = len(list) - 1)
# c = step (default = 1)

# set list cannot repeat the same value, the values cannot be changed in a set list, a set list is unordered
my_set = set(temp_list)
my_tuple = tuple(temp_list)
print('my_tuple:', my_tuple)
print('my_set:', my_set)
print('temp_list:', temp_list)
print('temp_list2:', temp_list2)


# empty strings are considered Falsy by default and non empty strings are considered Truthy

# 'type' is used to identify what the variable type is.
print(type(my_set))


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_powers = []






leaf_shinobi = Character(name = 'Naruto', age = '30')
leaf_shinobi.list_of_powers = ['rasengan', 'shadow clone']
print(leaf_shinobi.list_of_powers)
user_preference = input('What powers would you like to add?: ')
leaf_shinobi.list_of_powers.append(user_preference.lower()) if user_preference.lower() not in leaf_shinobi.list_of_powers else None
print(leaf_shinobi.list_of_powers)




