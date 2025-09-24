from __future__ import annotations
from domain.cart import Cart, LineItem
from domain.commands import AddItemCommand, RemoveItemCommand, ApplyPercentDiscountCommand, Command
from .invoker import CommandInvoker


def build_system():
    cart = Cart()
    invoker = CommandInvoker()
    return cart, invoker


def make_command(cart: Cart, spec: dict) -> Command:
    kind = spec.get("type")
    if kind == "add":
        return AddItemCommand(cart, LineItem(spec["sku"], int(spec["qty"]), float(spec["unit_price"])))
    if kind == "remove":
        return RemoveItemCommand(cart, spec["sku"], int(spec["qty"]))
    if kind == "percent":
        return ApplyPercentDiscountCommand(cart, float(spec["percent"]))
    raise ValueError(f"Unknown command type: {kind}")
