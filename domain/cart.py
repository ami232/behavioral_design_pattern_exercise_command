from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class LineItem:
    sku: str
    qty: int
    unit_price: float


class Cart:
    """Receiver in the Command pattern."""
    def __init__(self) -> None:
        # items: sku -> (qty, unit_price)
        self._items: Dict[str, Tuple[int, float]] = {}
        self.discount_percent: float = 0.0

    # --- item operations ---
    def add_item(self, sku: str, qty: int, unit_price: float) -> None:
        if qty <= 0:
            return
        if sku in self._items:
            existing_qty, existing_price = self._items[sku]
            if existing_price != unit_price:
                # For simplicity, keep original price
                unit_price = existing_price
            self._items[sku] = (existing_qty + qty, unit_price)
        else:
            self._items[sku] = (qty, unit_price)

    def remove_item(self, sku: str, qty: int) -> int:
        """Remove up to 'qty' items of sku. Returns actual removed qty."""
        if qty <= 0 or sku not in self._items:
            return 0
        existing_qty, price = self._items[sku]
        removed = min(qty, existing_qty)
        remaining = existing_qty - removed
        if remaining <= 0:
            del self._items[sku]
        else:
            self._items[sku] = (remaining, price)
        return removed

    # --- discount ---
    def set_discount_percent(self, percent: float) -> float:
        prev = self.discount_percent
        self.discount_percent = max(0.0, min(100.0, percent))
        return prev

    # --- totals ---
    def items(self) -> Dict[str, Tuple[int, float]]:
        return dict(self._items)

    def subtotal(self) -> float:
        return round(sum(q * p for q, p in self._items.values()), 2)

    def total(self) -> float:
        sub = self.subtotal()
        total = sub * (1.0 - self.discount_percent / 100.0)
        return round(total, 2)
