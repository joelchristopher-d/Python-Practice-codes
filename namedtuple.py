from collections import namedtuple

# Define namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20

# Access by index
print(p[0])  # Output: 10
