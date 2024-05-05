A = Semaphore(1)
B = semaphore(1)
C = Semaphore(1)

#Thread A
c.wait()
b.wait()
a.wait()

#critical section

a.signal()
c.signal()
b.signal


#Thread B
a.wait()
c.wait()
b.wait()

#critical section

b.signal()
a.signal()
c.signal


#Thread C
b.wait()
a.wait()
c.wait()

#critical section

c.signal()
b.signal()
a.signal