n = 3

count1 = Semaphore(3)

barrier1 = Semaphore(0)
barrier2 = Semaphore(1)
mutex = Semaphore(1)

## Thread A
mutex.wait()
count1.wait()
if count1.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
count1.signal()
barrier1.signal()
# critical section
mutex.wait()
if barrier2.n == 1-n:
    barrier1.wait()
    barrier2.signal()
mutex.signal()

barrier2.wait()
barrier2.signal()

##Thread B
mutex.wait()
count1.wait()
if count1.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
count1.signal()
barrier1.signal()
# critical section
mutex.wait()
if barrier2.n == 1-n:
    barrier1.wait()
    barrier2.signal()
mutex.signal()

barrier2.wait()
barrier2.signal()

##Thread C
mutex.wait()
count1.wait()
if count1.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
count1.signal()
barrier1.signal()
# critical section
mutex.wait()
if barrier2.n == 1-n:
    barrier1.wait()
    barrier2.signal()
mutex.signal()

barrier2.wait()
barrier2.signal()
