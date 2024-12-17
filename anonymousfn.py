# Regular function
def add(a, b):
    return a + b

# Lambda equivalent
add_lambda = lambda a, b: a + b
print(add_lambda(2, 3))  # Output: 5


nums = [1, 2, 3, 4, 5]

# Filter even numbers
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # Output: [2, 4]

nums = [1, 2, 3, 4, 5]

# Double each number
doubled = map(lambda x: x * 2, nums)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# from functools import reduce

nums = [1, 2, 3, 4, 5]

# Calculate product of all numbers
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120
