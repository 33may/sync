n = 4
barier1_check = Semaphore(n)
barier2_check = Semaphore(n)

barrier1 = Semaphore(0)
barrier2 = Semaphore(1)

## Thread A
barier1_check.wait()
if barier1_check.n == 0:
    barrier2.wait()
    barrier1.signal()
barrier1.wait()
barrier1.signal()
barier1_check.signal()
# critical section
barier2_check.wait()
if barier2_check.n == 0:
    barrier1.wait()
    barrier2.signal()

barrier2.wait()
barrier2.signal()
barier2_check.signal()

##Thread B
mutex.wait()
barier1_check.wait()
if barier1_check.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
barrier1.signal()
barier1_check.signal()
# critical section
mutex.wait()
barier2_check.wait()
if barier2_check.n == 0:
    barrier1.wait()
    barrier2.signal()
mutex.signal()

barrier2.wait()
barrier2.signal()
barier2_check.signal()

##Thread C
mutex.wait()
barier1_check.wait()
if barier1_check.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
barrier1.signal()
barier1_check.signal()
# critical section
mutex.wait()
barier2_check.wait()
if barier2_check.n == 0:
    barrier1.wait()
    barrier2.signal()
mutex.signal()

barrier2.wait()
barrier2.signal()
barier2_check.signal()


##Thread D
mutex.wait()
barier1_check.wait()
if barier1_check.n == 0:
    barrier2.wait()
    barrier1.signal()
mutex.signal()
barrier1.wait()
barrier1.signal()
barier1_check.signal()
# critical section
mutex.wait()
barier2_check.wait()
if barier2_check.n == 0:
    barrier1.wait()
    barrier2.signal() 
mutex.signal()

barrier2.wait()
barrier2.signal()
barier2_check.signal()