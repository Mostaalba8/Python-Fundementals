
class Wallet:
    def __init__(self, account_name: str):
        self.name = account_name
        self.balance = {}


    def can_spend(self, currency: str, amount: int) -> bool:
        existing_balance = self.balance.get(currency.upper(), 0)
        return amount <= existing_balance

    def deposit_money(self, currency: str, amount: int):
        self.balance[currency.upper()] = self.balance.get(currency.upper(), 0) + amount

    def spend_money(self, currency: str, amount: int):
        if not self.can_spend(currency, amount):
            return f'Insufficient funds, you have {self.balance.get(currency.upper())} {currency.upper()}'

        self.balance[currency.upper()] = self.balance.get(currency.upper(), 0) - amount
        return f'{amount} {currency.upper()} spent.'

    def give_money(self, other_wallet: "Wallet", currency: str, amount: int):
        if not self.can_spend(currency, amount):
            return f'Insufficient funds, you have {self.balance.get(currency.upper())} {currency}'

        other_wallet.deposit_money(currency, amount)
        self.spend_money(currency, amount)