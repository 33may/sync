import random
import time


forks = [Semaphore(1), Semaphore(1), Semaphore(1), Semaphore(1), Semaphore(1)]


## Thread A
# think
forks[0].wait()
forks[1].wait()
# eat
forks[0].signal()
forks[1].signal()

## Thread B
# think
forks[2].wait()
forks[1].wait()
# eat
forks[2].signal()
forks[1].signal()

## Thread C
# think
forks[2].wait()
forks[3].wait()
# eat
forks[2].signal()
forks[3].signal()

## Thread D
# think
forks[4].wait()
forks[3].wait()
# eat
forks[4].signal()
forks[3].signal()

## Thread E
# think
forks[4].wait()
forks[0].wait()
# eat
forks[4].signal()
forks[0].signal()














