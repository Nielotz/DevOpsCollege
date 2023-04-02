import numpy

def sub(a: float, b: float):
    return a - b

def multiply(a: float, b: float):
    return a * b

def divide(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def average(a: list):
    return numpy.average(a)
