# constructor - Methods used to initialise the members of the class when we create an instance
import part11_wallet
import part11_character

naruto = part11_character.Character(name='Naruto', age='30')
sasuke = part11_character.Character(name='Sasuke', age='29')

print(naruto.wallet.name)
print(sasuke.wallet.name)

print(f'Naruto wallet: {naruto.wallet.balance}')
print(f'Sasuke wallet: {sasuke.wallet.balance}')

naruto.wallet.deposit_money('gbp', 500)
naruto.wallet.deposit_money('eUr', 200)
print(f'Naruto wallet: {naruto.wallet.balance}')
naruto.wallet.spend_money('gbp', 200)
print(f'Naruto wallet: {naruto.wallet.balance}')
naruto.wallet.give_money(sasuke.wallet, 'gbp', 100)
print(f'Naruto wallet: {naruto.wallet.balance}')
print(f'Sasuke wallet: {sasuke.wallet.balance}')
sasuke.wallet.spend_money('gbp', 200)

