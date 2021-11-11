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

list_of_powers = {'rasengan':80, 'shadow clone':80, 'fireball':50, 'waterstyle':40}
print(list_of_powers)
wallet = {'GBP':1023, 'USD':130, 'EUR':320, 'BTC':0.02543222}
print(wallet)
print('')


def main():
    power_level_above(list_of_powers, 50)
    spend_from_wallet(wallet, 'gBp', 23)
    spend_from_wallet(wallet, 'bTc', 0.02)
    spend_from_wallet(wallet, 'USd', 2003)

def power_level_above(list, num):
    temp_list = []
    for i in list:
        if list[i] >= num:
            temp_list.append(i)
    print(temp_list)
    print('')


def spend_from_wallet(wallet_name, currency_name, amount):

    for i in wallet_name:
        if i.lower() == currency_name.lower():
            if wallet_name[i] >= amount:
                wallet_name[i] = wallet_name[i] - amount
                print('')
                print('Spending ' + i)
                print('Spent:')
                print(amount)
                print('Amount Left:')
                print(wallet_name[i])
                print('')
                break
            else:
                print('')
                print('Trying to spend:', amount)
                print('Insufficient amount in wallet for currency: ' + i)
                print('Amount left: ')
                print(wallet_name[i])
                print('')
                break
        elif wallet_name[i] != i:
            continue

        elif len(i) == len(wallet_name):
            print('')
            print('Currency ' + '"' + currency_name.lower() + '"' + ' does not exist in your wallet.')
            print('Currencies in wallet: ')
            print(wallet_name.keys())
            continue

    print('')
    print('Overall wallet after spendings: ')
    print(wallet_name)






main()