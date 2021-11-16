import pandas as pd
import part11_character
import csv

naruto = part11_character.Character(name='Naruto', age='30')
sasuke = part11_character.Character(name='Sasuke', age='29')

print(naruto.wallet.name)
print(naruto.wallet.balance)


with open('mybalance.csv') as csvfile:
    csv_balance = csv.DictReader(csvfile)

    for row in csv_balance:
        naruto.wallet.deposit_money(row['Currency'], int(row['Balance']))

print(naruto.wallet.balance)
