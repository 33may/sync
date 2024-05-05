n = 4
count = 0

barrier1 = Semaphore(0)
barrier2 = Semaphore(0)
mutex = Semaphore(1)

## Thread A
mutex.wait()
count += 1
if count == n:
    barrier1.signal()
    mutex.signal()
    barrier1.wait()
else:
    mutex.signal()
    barrier1.wait()
    barrier1.signal()

# critical section
mutex.wait()
count -= 1
if count == 0:
    barrier2.signal()
    mutex.signal()
    barrier2.wait()
else:
    mutex.signal()
    barrier2.wait()
    barrier2.signal()


##Thread B
mutex.wait()
count += 1
if count == n:
    barrier1.signal()
    mutex.signal()
    barrier1.wait()
else:
    mutex.signal()
    barrier1.wait()
    barrier1.signal()

# critical section
mutex.wait()
count -= 1
if count == 0:
    barrier2.signal()
    mutex.signal()
    barrier2.wait()
else:
    mutex.signal()
    barrier2.wait()
    barrier2.signal()

##Thread C
mutex.wait()
count += 1
if count == n:
    barrier1.signal()
    mutex.signal()
    barrier1.wait()
else:
    mutex.signal()
    barrier1.wait()
    barrier1.signal()

# critical section
mutex.wait()
count -= 1
if count == 0:
    barrier2.signal()
    mutex.signal()
    barrier2.wait()
else:
    mutex.signal()
    barrier2.wait()
    barrier2.signal()


##Thread D
mutex.wait()
count += 1
if count == n:
    barrier1.signal()
    mutex.signal()
    barrier1.wait()
else:
    mutex.signal()
    barrier1.wait()
    barrier1.signal()

# critical section
mutex.wait()
count -= 1
if count == 0:
    barrier2.signal()
    mutex.signal()
    barrier2.wait()
else:
    mutex.signal()
    barrier2.wait()
    barrier2.signal()