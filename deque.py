from collections import deque

# Creating an empty deque
dq = deque()

# Creating a deque with initial elements
dq = deque([7])
print(dq)  # Output: deque([1, 2, 3, 4, 5])

# Creating a deque with a maximum length
dq = deque("jgjgjgjh", maxlen=5)
print(dq)  # Output: deque([1, 2, 3], maxlen=5)
