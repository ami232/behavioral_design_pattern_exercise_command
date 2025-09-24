# Command Pattern Exercise - Solution Guide

This file contains the solution implementations for instructors. **Do not share with students.**

## Commands Implementation (`domain/commands.py`)

### AddItemCommand

```python
def execute(self) -> None:
    self.cart.add_item(self.item.sku, self.item.qty, self.item.unit_price)

def undo(self) -> None:
    self.cart.remove_item(self.item.sku, self.item.qty)
```

### RemoveItemCommand

```python
def execute(self) -> None:
    if self.sku in self.cart.items():
        self._unit_price = self.cart.items()[self.sku][1]
    self._actually_removed = self.cart.remove_item(self.sku, self.qty)

def undo(self) -> None:
    if self._actually_removed > 0 and self._unit_price is not None:
        self.cart.add_item(self.sku, self._actually_removed, self._unit_price)
```

### ApplyPercentDiscountCommand

```python
def execute(self) -> None:
    self._prev = self.cart.set_discount_percent(self.percent)

def undo(self) -> None:
    if self._prev is not None:
        self.cart.set_discount_percent(self._prev)
```

## CommandInvoker Implementation (`application/invoker.py`)

```python
def run(self, cmd: Command) -> None:
    cmd.execute()
    self._history.append(cmd)
    self._redo.clear()

def undo(self, n: int = 1) -> int:
    undone = 0
    while n > 0 and self._history:
        cmd = self._history.pop()
        cmd.undo()
        self._redo.append(cmd)
        n -= 1
        undone += 1
    return undone

def redo(self, n: int = 1) -> int:
    redone = 0
    while n > 0 and self._redo:
        cmd = self._redo.pop()
        cmd.execute()
        self._history.append(cmd)
        n -= 1
        redone += 1
    return redone
```

## Key Learning Points

1. **State for Undo**: Commands must store information during execute() to properly undo
2. **RemoveItemCommand Complexity**: Must track actual removed quantity and unit price
3. **History Management**: Clear redo stack when new command is executed
4. **Return Values**: Undo/redo methods return count of operations performed

## Common Student Mistakes

1. Not storing state in RemoveItemCommand for proper undo
2. Forgetting to clear redo stack in run() method
3. Not handling edge cases (empty stacks, partial removals)
4. Not returning the correct count from undo/redo methods