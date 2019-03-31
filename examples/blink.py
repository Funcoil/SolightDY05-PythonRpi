#!/usr/bin/python

import time
import pigpio
from dy05 import DY05

def main():
    dy05 = DY05(pigpio.pi(), 17)

    address = 42
    socket = 1

    while True:
        dy05.send(address, socket, 1);
        time.sleep(1)
        dy05.send(address, socket, 0);
        time.sleep(1)

if __name__ == "__main__":
    main()
