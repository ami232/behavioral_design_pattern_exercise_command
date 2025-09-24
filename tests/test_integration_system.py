from application.bootstrap import build_system, make_command


def test_system_with_undo_redo():
    cart, invoker = build_system()
    cmds = [
        {"type": "add", "sku": "A", "qty": 2, "unit_price": 10.0},   # +20
        {"type": "add", "sku": "B", "qty": 5, "unit_price": 3.0},    # +15 => 35
        {"type": "percent", "percent": 10},                                 # 10% => 31.5
        {"type": "remove", "sku": "B", "qty": 2},                       # remove 2*3 => subtotal 29, total 26.1
    ]
    for spec in cmds:
        invoker.run(make_command(cart, spec))

    assert cart.subtotal() == 29.0
    assert cart.total() == 26.1

    invoker.undo(2)
    assert cart.subtotal() == 35.0
    assert cart.total() == 35.0

    invoker.redo(2)
    assert cart.subtotal() == 29.0
    assert cart.total() == 26.1
