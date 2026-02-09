
from collections import deque

# Deque are used when you need operation from both sides
#Its used in stack, queue too
dq = deque([2,3,1])

dq.append(7)
print(dq) #[2,3,1,7]

dq.appendleft(5)
print(dq) #[5,2,3,1,7]

print(dq.pop()) #7
print(dq) #[5,2,3,1]

print(dq.popleft()) #5
print(dq) #[2,3,1]

dq.append([4,5]) #This will add as list
print(dq)

dq.extend([4,5]) #this fix above mess
print(dq)

dq.extendleft([-1,-2]) #[-2,-1,2,3,1,....]
print(dq)

dq.rotate(2)
print(dq) # move elementes to right side