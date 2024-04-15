"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None):
        self.stdout = stdout
        self.stderr = stderr
        self.old_stdout = None
        self.old_stderr = None

    def __enter__(self):
        import sys
        if self.stdout:
            self.old_stdout = sys.stdout
            sys.stdout = self.stdout
        if self.stderr:
            self.old_stderr = sys.stderr
            sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        import sys
        if self.stdout:
            sys.stdout = self.old_stdout
        if self.stderr:
            sys.stderr = self.old_stderr
        if exc_type is not None:
            print(exc_val, file=self.stderr)
        return True

# Тесты
if __name__ == "__main__":
    import sys

    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        try:
            raise Exception('Hello stderr.txt')
        except Exception as ex:
            print(ex, file=sys.stderr)

    print('Hello stdout again')
    raise Exception('Hello stderr')