import logging
import random
import threading
import time
from typing import List

total_tickets: int = 10

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Director(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        logger.info('Director started work')

    def run(self) -> None:
        global total_tickets
        while total_tickets < 9:
            with self.sem:
                logger.info('Director is printing more tickets!')
                total_tickets += 6
                logger.info(f'Number of tickets after printing: {total_tickets}')
                time.sleep(2)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.tickets_sold: int = 0
        logger.info('Seller started work')

    def run(self) -> None:
        global total_tickets
        is_running: bool = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if total_tickets <= 0:
                    break
                self.tickets_sold += 1
                total_tickets -= 1
                logger.info(f'{self.name} sold one; {total_tickets} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self) -> None:
        time.sleep(random.randint(0, 1))


def main() -> None:
    semaphore: threading.Semaphore = threading.Semaphore()
    sellers: List[Seller] = []
    director = Director(semaphore)
    director.start()

    for _ in range(3):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    director.join()

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()