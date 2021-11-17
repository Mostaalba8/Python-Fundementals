import pytest
from part11_wallet import Wallet
from part11_character import Character

from part13 import square_root

test_wallet = Wallet('Mostafa')
test_wallet.deposit_money('GBP', 10)
receiving_wallet = Wallet('TestWallet')


def test_valid_input_with_valid_response():
    assert square_root(4) == 2


def test_negative_square_root():
    with pytest.raises(ValueError):
        square_root(-4)


def test_wallet_spend_money():
    assert test_wallet.balance.get('GBP') == 10
    test_wallet.spend_money('GBP', 5)
    assert test_wallet.balance.get('GBP') == 5


def test_wallet_deposit_money():
    assert test_wallet.balance.get('GBP') == 5
    test_wallet.deposit_money('GBP', 100)
    assert test_wallet.balance['GBP'] == 105


def test_wallet_spending_too_much():
    assert test_wallet.spend_money('GBP', 200) == f'Insufficient funds, you have {test_wallet.balance.get("GBP")} GBP'


def test_using_non_capital_letters_for_currency():
    assert test_wallet.balance.get('GBP') == 105
    test_wallet.deposit_money('gbp', 10)
    test_wallet.deposit_money('GbP', 10)
    test_wallet.deposit_money('GBp', 10)
    assert test_wallet.balance.get('GBP') == 135


def test_sending_money_to_another_wallet():
    assert test_wallet.balance.get('GBP') == 135
    assert receiving_wallet.balance.get('GBP',0) == 0
    test_wallet.give_money(receiving_wallet,'GBP', 100)
    assert test_wallet.balance.get('GBP') == 35
    assert receiving_wallet.balance.get('GBP') == 100
