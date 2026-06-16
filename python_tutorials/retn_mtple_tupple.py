'''Write a function that returns multiple values (as a tuple) and show how to unpack them.'''


def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

result1, result2, result3 = calculate(10, 5)

print(result1)
print(result2)
print(result3)