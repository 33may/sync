# deadlock example

aArrived = Semaphore(1)
bArrived = Semaphore(0)
cArrived = Semaphore(0)
dArrived = Semaphore(0)

## Thread A

aArrived.wait()
print(1)
bArrived.signal()
aArrived.wait()
print(5)
bArrived.signal()

##Thread B
bArrived.wait()
print(2)
cArrived.signal()
bArrived.wait()
print(6)
cArrived.signal()

##Thread C
cArrived.wait()
print(3)
dArrived.signal()
cArrived.wait()
print(7)
dArrived.signal()


##Thread D
dArrived.wait()
print(4)
aArrived.signal()
dArrived.wait()
print(8)
aArrived.signal()