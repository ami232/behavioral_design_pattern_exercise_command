from __future__ import annotations
from typing import List
from domain.commands import Command


class CommandInvoker:
    """Invoker that maintains undo/redo stacks."""
    def __init__(self) -> None:
        self._history: List[Command] = []
        self._redo: List[Command] = []

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
