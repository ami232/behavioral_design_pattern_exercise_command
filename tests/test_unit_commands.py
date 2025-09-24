from domain.cart import Cart, LineItem
from domain.commands import AddItemCommand, RemoveItemCommand, ApplyPercentDiscountCommand


def test_add_and_undo():
    cart = Cart()
    add = AddItemCommand(cart, LineItem("A", 2, 10.0))
    add.execute()
    assert cart.items()["A"] == (2, 10.0)
    assert cart.subtotal() == 20.0

    add.undo()
    assert "A" not in cart.items()
    assert cart.subtotal() == 0.0


def test_remove_and_undo():
    cart = Cart()
    AddItemCommand(cart, LineItem("B", 5, 3.0)).execute()  # subtotal 15
    rem = RemoveItemCommand(cart, "B", 3)
    rem.execute()
    assert cart.items()["B"][0] == 2
    assert cart.subtotal() == 6.0

    rem.undo()
    assert cart.items()["B"][0] == 5
    assert cart.subtotal() == 15.0


def test_apply_discount_and_undo():
    cart = Cart()
    AddItemCommand(cart, LineItem("A", 2, 10.0)).execute()  # subtotal 20
    disc = ApplyPercentDiscountCommand(cart, 10)
    disc.execute()
    assert cart.discount_percent == 10
    assert cart.total() == 18.0

    disc.undo()
    assert cart.discount_percent == 0
    assert cart.total() == 20.0
