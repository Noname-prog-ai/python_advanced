import unittest
from typing import Collection, Type, Literal
from types import TracebackType
from block_errors import BlockErrors

class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        pass

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if exc_type is not None and issubclass(exc_type, tuple(self.errors)):
            return True
        return None

if __name__ == '__main__':
    unittest.main()
