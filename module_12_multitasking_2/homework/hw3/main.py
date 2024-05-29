import threading
from threading import Semaphore, Thread
import time
import signal
import sys

sem = Semaphore()

def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)

def signal_handler(sig, frame):
    print('\nreceived keyboard interrupt, quitting threads.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

t1 = threading.Thread(target=fun1, daemon=True)
t2 = threading.Thread(target=fun2, daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()