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
        self.cart.add_item(self.item.sku, self.item.qty, self.item.unit_price)

    def undo(self) -> None:
        self.cart.remove_item(self.item.sku, self.item.qty)


@dataclass
class RemoveItemCommand(Command):
    cart: Cart
    sku: str
    qty: int
    _actually_removed: int = 0
    _unit_price: Optional[float] = None

    def execute(self) -> None:
        if self.sku in self.cart.items():
            self._unit_price = self.cart.items()[self.sku][1]
        self._actually_removed = self.cart.remove_item(self.sku, self.qty)

    def undo(self) -> None:
        if self._actually_removed > 0 and self._unit_price is not None:
            self.cart.add_item(self.sku, self._actually_removed, self._unit_price)


@dataclass
class ApplyPercentDiscountCommand(Command):
    cart: Cart
    percent: float
    _prev: Optional[float] = None

    def execute(self) -> None:
        self._prev = self.cart.set_discount_percent(self.percent)

    def undo(self) -> None:
        if self._prev is not None:
            self.cart.set_discount_percent(self._prev)
