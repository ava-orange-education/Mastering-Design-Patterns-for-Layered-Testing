import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item_to_cart(cart):
    cart.add_item("apple", 3)
    assert cart.total_items() == 3
    assert cart.total_cost() == 9  # Assuming the cost of an apple is $3