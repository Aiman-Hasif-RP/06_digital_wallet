import pytest
from src.wallet_affordability import can_afford


def test_can_afford_balance_above_price_valid():
    # Arrange
    balance_cents = 1001
    price_cents = 1000

    # Act
    result = can_afford(balance_cents, price_cents)

    # Assert
    assert result is True


def test_can_afford_balance_equal_to_price_valid():
    # Arrange
    balance_cents = 1000
    price_cents = 1000

    # Act
    result = can_afford(balance_cents, price_cents)

    # Assert
    assert result is True


def test_can_afford_balance_below_price_valid():
    # Arrange
    balance_cents = 999
    price_cents = 1000

    # Act
    result = can_afford(balance_cents, price_cents)

    # Assert
    assert result is False


def test_can_afford_zero_price_valid():
    # Arrange
    balance_cents = 1000
    price_cents = 0

    # Act
    result = can_afford(balance_cents, price_cents)

    # Assert
    assert result is True


def test_can_afford_zero_balance_and_zero_price_valid():
    # Arrange
    balance_cents = 0
    price_cents = 0

    # Act
    result = can_afford(balance_cents, price_cents)

    # Assert
    assert result is True


def test_can_afford_negative_balance_invalid():
    # Arrange
    balance_cents = -1
    price_cents = 100

    # Act and Assert
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)


def test_can_afford_negative_price_invalid():
    # Arrange
    balance_cents = 1000
    price_cents = -1

    # Act and Assert
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)


@pytest.mark.parametrize(
    "balance_cents",
    [
        "1000",   # String
        1000.0,   # Float
        True,     # Boolean
    ],
)
def test_can_afford_balance_type_invalid(balance_cents):
    # Arrange
    # balance_cents is supplied by parameterisation.
    price_cents = 100

    # Act and Assert
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)


@pytest.mark.parametrize(
    "price_cents",
    [
        "100",   # String
        100.0,   # Float
        True,    # Boolean
    ],
)
def test_can_afford_price_type_invalid(price_cents):
    # Arrange
    balance_cents = 1000
    # price_cents is supplied by parameterisation.

    # Act and Assert
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)