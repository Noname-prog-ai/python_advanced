"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
from typing import List

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.info("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.info("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.info("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.info(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.info(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.info(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.info(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.info(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.info("Leave measure_me")

    return results


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        filename='logger.txt',
        filemode='w',
        format="%(asctime)s.%(msecs)03d - %(message)s",
        datefmt='%M:%S',
    )
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)
