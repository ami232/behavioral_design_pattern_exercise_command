# Command Pattern Example (Cart)

This project demonstrates the **Command** behavioral pattern using a simple shopping cart.
Commands encapsulate actions (add/remove item, apply percent discount) with **undo/redo** support.

## Structure

```
command_app/
├─ domain/
│  ├─ cart.py            # Receiver (Cart) and LineItem
│  └─ commands.py        # Command interface + concrete commands
├─ application/
│  ├─ invoker.py         # CommandInvoker with history + redo stacks
│  └─ bootstrap.py       # Wiring helpers
├─ presentation/
│  └─ cli.py             # CLI entry point
└─ tests/                # Unit + integration tests (pytest)
```

## CLI Usage

```bash
python -m command_app.presentation.cli --cmds '[
  {"type":"add","sku":"A","qty":2,"unit_price":10.0},
  {"type":"add","sku":"B","qty":5,"unit_price":3.0},
  {"type":"percent","percent":10},
  {"type":"remove","sku":"B","qty":2}
]' --undo 2 --redo 2

# Items:
#  - A: qty=2, unit_price=10.00
#  - B: qty=3, unit_price=3.00
# Discount: 10.0%
# Subtotal: 29.00
# Total: 26.10
```

## Tests

```bash
pip install pytest
pytest -q command_app/tests
```
