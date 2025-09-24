from __future__ import annotations
from typing import List
from domain.commands import Command


class CommandInvoker:
    """Invoker that maintains undo/redo stacks."""
    def __init__(self) -> None:
        self._history: List[Command] = []
        self._redo: List[Command] = []

    def run(self, cmd: Command) -> None:
        # TODO: Implement - execute the command and manage history
        # Hint: Execute the command, add it to history, and clear redo stack
        pass

    def undo(self, n: int = 1) -> int:
        # TODO: Implement - undo the last n commands
        # Hint: Pop commands from history, call their undo(), move to redo stack
        # Return the number of commands actually undone
        pass

    def redo(self, n: int = 1) -> int:
        # TODO: Implement - redo the last n undone commands  
        # Hint: Pop commands from redo stack, execute them, move back to history
        # Return the number of commands actually redone
        pass
