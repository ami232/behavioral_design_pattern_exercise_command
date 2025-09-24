from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from .cart import Cart, LineItem


class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...


@dataclass
class AddItemCommand(Command):
    cart: Cart
    item: LineItem

    def execute(self) -> None:
        # TODO: Implement - add the item to the cart
        pass

    def undo(self) -> None:
        # TODO: Implement - remove the item from the cart to undo the add operation
        pass


@dataclass
class RemoveItemCommand(Command):
    cart: Cart
    sku: str
    qty: int
    _actually_removed: int = 0
    _unit_price: Optional[float] = None

    def execute(self) -> None:
        # TODO: Implement - remove the item from cart and store information needed for undo
        # Hint: You'll need to track what was actually removed and the unit price
        pass

    def undo(self) -> None:
        # TODO: Implement - restore the removed items to the cart
        # Hint: Use the information stored during execute()
        pass


@dataclass
class ApplyPercentDiscountCommand(Command):
    cart: Cart
    percent: float
    _prev: Optional[float] = None

    def execute(self) -> None:
        # TODO: Implement - apply the discount and store the previous value for undo
        pass

    def undo(self) -> None:
        # TODO: Implement - restore the previous discount percentage
        pass
