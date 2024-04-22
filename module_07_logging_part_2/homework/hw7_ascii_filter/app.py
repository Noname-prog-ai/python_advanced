import sys
import logging
from utils import string_to_operator


logger = logging.getLogger('app')
logger.setLevel("INFO")
formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def calc(args):
    logger.debug("Кириллические символы")
    logger.debug('ASCII symbols')
    logger.info(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    logger.info(f"Result: {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+3')
