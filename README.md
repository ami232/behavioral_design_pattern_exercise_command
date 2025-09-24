# Command Pattern Implementation Exercise

## Learning Objectives

By completing this exercise, you will:

1. **Understand the Command Pattern**: Learn how to encapsulate requests as objects, allowing you to parameterize clients with different requests, queue operations, and support undo operations.

2. **Implement Undoable Operations**: Practice creating commands that can be both executed and undone, maintaining state necessary for reversible operations.

3. **Build Command History Management**: Implement an invoker that manages command execution history and supports undo/redo functionality.

4. **Apply SOLID Principles**: Work with well-structured code that demonstrates single responsibility, open/closed principle, and dependency inversion.

## Exercise Overview

You are working with a shopping cart system that uses the **Command Pattern** to handle operations like adding items, removing items, and applying discounts. The system supports undo and redo functionality, making it easy to reverse operations.

### Architecture Components

The application follows the Command Pattern with these key components:

- **Command Interface** (`Command`): Abstract base class defining `execute()` and `undo()` methods
- **Concrete Commands**: Specific implementations for cart operations:
  - `AddItemCommand`: Adds items to the cart
  - `RemoveItemCommand`: Removes items from the cart
  - `ApplyPercentDiscountCommand`: Applies percentage discounts
- **Receiver** (`Cart`): The object that performs the actual work
- **Invoker** (`CommandInvoker`): Manages command execution and maintains undo/redo history
- **Client** (`cli.py`): Creates and configures commands

## What You Need to Implement

Your task is to implement the missing functionality in the following methods:

### 1. Command Implementations (`domain/commands.py`)

#### `AddItemCommand`
- **`execute()`**: Add the item to the cart
- **`undo()`**: Remove the item from the cart to reverse the add operation

#### `RemoveItemCommand`  
- **`execute()`**: Remove items from the cart and store information needed for undo
- **`undo()`**: Restore the removed items to the cart

#### `ApplyPercentDiscountCommand`
- **`execute()`**: Apply the discount percentage and store the previous value
- **`undo()`**: Restore the previous discount percentage

### 2. Command Invoker (`application/invoker.py`)

#### `CommandInvoker`
- **`run(cmd)`**: Execute the command and manage history
- **`undo(n)`**: Undo the last n commands, return count of commands actually undone
- **`redo(n)`**: Redo the last n undone commands, return count of commands actually redone

## Implementation Hints

### For Commands:
1. **State Management**: Commands that need to be undoable must store enough information during `execute()` to reverse their effects in `undo()`
2. **RemoveItemCommand Complexity**: When removing items, you need to track:
   - How many items were actually removed (might be less than requested)
   - The unit price of removed items (for restoration)
3. **Discount Command**: The cart's `set_discount_percent()` method returns the previous discount value

### For Invoker:
1. **History Management**: Maintain two stacks - one for executed commands (history) and one for undone commands (redo)
2. **Undo Logic**: Pop from history, call `undo()`, push to redo stack
3. **Redo Logic**: Pop from redo stack, call `execute()`, push to history
4. **State Clearing**: When a new command is executed, clear the redo stack

## Available Cart Methods

The `Cart` class provides these methods for your implementations:

```python
# Item operations
cart.add_item(sku: str, qty: int, unit_price: float) -> None
cart.remove_item(sku: str, qty: int) -> int  # Returns actual removed quantity

# Discount operations  
cart.set_discount_percent(percent: float) -> float  # Returns previous percentage

# Query operations
cart.items() -> Dict[str, Tuple[int, float]]  # Returns {sku: (qty, unit_price)}
cart.subtotal() -> float
cart.total() -> float  # Subtotal with discount applied
```

## Testing Your Implementation

### Running Unit Tests
```bash
python -m pytest tests/test_unit_commands.py -v
```

### Running Integration Tests  
```bash
python -m pytest tests/ -v
```

### Manual Testing via CLI
```bash
# Add items and apply discount
python -m presentation.cli --cmds '[{"type":"add","sku":"A","qty":2,"unit_price":10.0},{"type":"percent","percent":10}]'

# Test with undo/redo
python -m presentation.cli --cmds '[{"type":"add","sku":"A","qty":2,"unit_price":10.0}]' --undo 1 --redo 1
```

## Expected Behavior

When fully implemented:

1. **Commands execute correctly**: Items are added/removed, discounts applied
2. **Undo works perfectly**: All operations can be reversed
3. **Redo functionality**: Undone operations can be redone
4. **State consistency**: Cart state is always consistent after any sequence of operations
5. **History management**: Command history is properly maintained

## Success Criteria

Your implementation is complete when:
- [ ] All unit tests pass
- [ ] All integration tests pass  
- [ ] CLI operations work correctly with undo/redo
- [ ] Commands properly store state needed for undo operations
- [ ] Invoker correctly manages command history and redo stack

## Project Structure

```
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── application/
│   ├── bootstrap.py             # System setup and command factory
│   └── invoker.py              # Command invoker (implement this)
├── domain/
│   ├── cart.py                 # Cart implementation (complete)
│   └── commands.py             # Command implementations (implement this)
├── presentation/
│   └── cli.py                  # Command-line interface (complete)
└── tests/
    ├── test_unit_commands.py   # Unit tests for commands
    ├── test_integration_cli.py # CLI integration tests
    └── test_integration_system.py # System integration tests
```

## Additional Resources

- [Command Pattern - Gang of Four](https://en.wikipedia.org/wiki/Command_pattern)
- [Python ABC Module Documentation](https://docs.python.org/3/library/abc.html)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)

Good luck with your implementation! Remember to think about what information each command needs to store to support proper undo functionality.
