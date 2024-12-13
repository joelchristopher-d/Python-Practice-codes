def infinite_generator():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_generator()
print(next(gen)) 
print(next(gen))  


def coroutine_example():
    while True:
        value = yield
        print(f"Received: {value}")

cor = coroutine_example()
next(cor) 
cor.send("Hello")  
cor.send("World")  


def range_generator(start, end):
    for i in range(start, end):
        yield i

for num in range_generator(1, 5):
    print(num)  


def my_generator():
    print("First")
    yield 1  # Pauses here
    print("Second")
    yield 2  # Pauses here
    print("Third")
    yield 3

gen = my_generator()
print(next(gen))  
print(next(gen))  
print(next(gen))  
