from functools import reduce
def add(a, b):
    return a + b
numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print("sum of numbers:",total)