import pytest
from src.wallet_withdrawal import withdraw


def test_withdraw_normal_amount_valid():
    # Arrange
    balance_cents = 1000
    amount_cents = 300
    expected_balance = 700

    # Act
    result = withdraw(balance_cents, amount_cents)

    # Assert
    assert result == expected_balance
    assert type(result) is int


def test_withdraw_minimum_exact_balance_valid():
    # Arrange
    balance_cents = 1
    amount_cents = 1

    # Act
    result = withdraw(balance_cents, amount_cents)

    # Assert
    assert result == 0
    assert type(result) is int


def test_withdraw_negative_balance_invalid():
    # Arrange
    balance_cents = -1
    amount_cents = 1

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


def test_withdraw_zero_amount_invalid():
    # Arrange
    balance_cents = 1000
    amount_cents = 0

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


def test_withdraw_negative_amount_invalid():
    # Arrange
    balance_cents = 1000
    amount_cents = -1

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


def test_withdraw_amount_above_balance_invalid():
    # Arrange
    balance_cents = 1000
    amount_cents = 1001

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


def test_withdraw_from_zero_balance_invalid():
    # Arrange
    balance_cents = 0
    amount_cents = 1

    # Act and Assert
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(
    "balance_cents",
    [
        "1000",   # String
        1000.0,   # Float
        True,     # Boolean
    ],
)
def test_withdraw_balance_type_invalid(balance_cents):
    # Arrange
    # balance_cents is supplied by parameterisation.
    amount_cents = 100

    # Act and Assert
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(
    "amount_cents",
    [
        "100",   # String
        100.0,   # Float
        True,    # Boolean
    ],
)
def test_withdraw_amount_type_invalid(amount_cents):
    # Arrange
    balance_cents = 1000
    # amount_cents is supplied by parameterisation.

    # Act and Assert
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)