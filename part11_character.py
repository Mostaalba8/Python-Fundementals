from part11_wallet import Wallet


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wallet = Wallet(account_name=f"{self.name}'s wallet")
