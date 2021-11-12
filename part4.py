# types of loops in Python
# for loops and while loops
# x = 0
#
# # while loop
# while (x <= 5):
#     print(x)
#     x += 1
#
# # for loop
# for x in range(5, 10):
#     print(x)
#
# # for loop iterating through an array
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for x in days:
#     print(x)
#
#
# for letter in "Mostafa":
#     print(letter)
list_of_powers = {'rasengan': 80, 'shadow clone': 80, 'fireball': 50, 'waterstyle': 40}
print(list_of_powers)
wallet = {'GBP': 1023, 'USD': 130, 'EUR': 320, 'BTC': 0.02543222}
print(wallet)
print('')


def main():
    power_level_above(list_of_powers, 50)
    spend_from_wallet(wallet, 'GBP', 10)
    spend_from_wallet(wallet, 'bTc', 0.4)
    spend_from_wallet(wallet, 'USd', 30)
    spend_from_wallet(wallet, 'udS', 2003)


def power_level_above(list, num):
    temp_list = []
    for i in list:
        if list[i] >= num:
            temp_list.append(i)
    print(temp_list)
    print('')
    return temp_list


def spend_from_wallet(wallet, currency, amount):
    currency = currency.upper()
    can_spend = min(amount, wallet.get(currency, 0))
    wallet[currency] = wallet.get(currency, 0) - can_spend
    print(can_spend)
    return can_spend


main()