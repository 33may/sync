leader = Semaphore(1)
leader_Queue = Semaphore(1)
follower = Semaphore(1)
follower_Queue = Semaphore(1)

## Thread L1
leader_Queue.wait()
follower.signal()
leader.wait()
# dance
leader_Queue.signal()

##Thread F1
follower_Queue.wait()
leader.signal()
follower.wait()
# dance
follower_Queue.signal()

## Thread L1
leader_Queue.wait()
follower.signal()
leader.wait()
# dance
leader_Queue.signal()

##Thread F1
follower_Queue.wait()
leader.signal()
follower.wait()
# dance
follower_Queue.signal()

## Thread L1
leader_Queue.wait()
follower.signal()
leader.wait()
# dance
leader_Queue.signal()

##Thread F1
follower_Queue.wait()
leader.signal()
follower.wait()
# dance
follower_Queue.signal()

## Thread L1
leader_Queue.wait()
follower.signal()
leader.wait()
# dance
leader_Queue.signal()

##Thread F1
follower_Queue.wait()
leader.signal()
follower.wait()
# dance
follower_Queue.signal()
