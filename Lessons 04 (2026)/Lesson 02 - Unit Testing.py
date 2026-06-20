"""
Educational example: Unit Testing with pytest
PyCharm is running the file through pytest discovery, because of keywords like class TestSomething and/or def test_something().
It effectively runs: pytest your_file.py
So, Python never reaches __main__.

Notice:
PyCharm is running “context-sensitive run” (Run gutter / caret-based execution), not a fixed run configuration.

This file demonstrates:
- Testing business logic in isolation → testing units of code without involving other systems like databases, APIs, files, or networks.
- Positive, negative, and edge-case scenarios → test different “types” of inputs, i.e. 100 / -100 / 0.
- Exception testing → checks that the code fails correctly when it should.
- Parametrized tests → run one test with multiple inputs, instead of writing many similar tests, i.e. @pytest.mark.parametrize.
- Arrange -> Act -> Assert pattern → a structure for writing clean tests.
"""


import pytest
from enum import Enum


# =====================================================
# Production Code
# =====================================================

class CustomerType(Enum):
    REGULAR = "regular"
    PREMIUM = "premium"
    VIP = "vip"


def calculate_discount(
    customer_type: CustomerType,
    order_amount: float,
    years_as_customer: int,
) -> float:

    if order_amount < 0:
        raise ValueError("order_amount cannot be negative")
    if years_as_customer < 0:
        raise ValueError("years_as_customer cannot be negative")

    discount = 0
    if customer_type == CustomerType.VIP:
        discount += 20
    elif customer_type == CustomerType.PREMIUM:
        discount += 10
    elif customer_type == CustomerType.REGULAR:
        discount += 0
    else:
        raise ValueError("unknown customer type")

    if years_as_customer >= 5:
        discount += 5
    if order_amount > 1000:
        discount += 3
    return min(discount, 30)


def final_price(
    customer_type: CustomerType,
    order_amount: float,
    years_as_customer: int,
) -> float:
    discount = calculate_discount(customer_type, order_amount, years_as_customer)
    return round(order_amount * (1 - discount / 100), 2)


# =====================================================
# Tests
# =====================================================

class TestCalculateDiscount:

    def test_regular_customer_has_no_discount(self):
        # Arrange
        customer = CustomerType.REGULAR
        # Act
        result = calculate_discount(customer, order_amount=100, years_as_customer=1)
        # Assert
        assert result == 0

    def test_premium_customer_discount(self):
        result = calculate_discount(CustomerType.PREMIUM, 100, 1)
        assert result == 10

    def test_vip_customer_discount(self):
        result = calculate_discount(CustomerType.VIP, 100, 1)
        assert result == 20

    def test_loyal_customer_bonus(self):
        result = calculate_discount(CustomerType.REGULAR, 100, 5)
        assert result == 5

    def test_large_order_bonus(self):
        result = calculate_discount(CustomerType.REGULAR, 1500, 1)
        assert result == 3

    def test_multiple_bonuses_accumulate(self):
        result = calculate_discount(CustomerType.PREMIUM, 2000, 10)
        assert result == 18

    def test_discount_is_capped(self):
        result = calculate_discount(CustomerType.VIP, 100000, 50)
        assert result == 28


class TestValidation:

    def test_negative_order_amount(self):
        with pytest.raises(ValueError):
            calculate_discount(CustomerType.REGULAR, -1, 1)

    def test_negative_years(self):
        with pytest.raises(ValueError):
            calculate_discount(CustomerType.REGULAR, 100, -1)


class TestFinalPrice:

    def test_final_price_for_vip(self):
        result = final_price(CustomerType.VIP, 100, 0)
        assert result == 80.0

    def test_final_price_with_multiple_discounts(self):
        result = final_price(CustomerType.PREMIUM, 2000, 5)
        assert result == 1640.0


@pytest.mark.parametrize(
    "customer,amount,years,expected",
    [
        (CustomerType.REGULAR, 100, 0, 0),
        (CustomerType.PREMIUM, 100, 0, 10),
        (CustomerType.VIP, 100, 0, 20),
        (CustomerType.REGULAR, 100, 5, 5),
        (CustomerType.REGULAR, 1500, 0, 3),
    ],
)
def test_discount_scenarios(customer, amount, years, expected):
    assert (calculate_discount(customer, amount, years) == expected)


if __name__ == "__main__":
    print("__main__")
    print(final_price(CustomerType.PREMIUM, 2000, 5))
