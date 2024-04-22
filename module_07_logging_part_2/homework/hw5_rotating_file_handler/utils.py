import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add

from module_07_logging_part_2.homework.hw5_rotating_file_handler.config import dict_config

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}
Numeric = Union[int, float]
logger = logging.getLogger('utils')
logger.setLevel("ERROR")
formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
logging.config.dictConfig(dict_config)
logger = logging.getLogger('my_logger.utils')


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    logger.info(f"Преобразование строкового символа: '{value}")
    if not isinstance(value, str):
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
