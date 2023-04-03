import numpy

def sub(a: float, b: float):
    return a - b

def mul(a: float, b: float):
    return a * b

def div(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def avg(a: list):
    return numpy.average(a)
 