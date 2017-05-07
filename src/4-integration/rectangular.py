import sys

sys.path.append('../../libs/')
from functiontools import function
from integralutil import get_interval_points

def rectangular(dx, fs):

    integral = 0.0
    for y in fs:
        integral+=y
    
    integral *= dx
    return integral

if __name__ == "__main__":
    n = int(input("Enter n: "))
    intLimits = [float(x) for x in input("Please enter integration limits: ").split(' ')]
    expr = input("Please give the function to be integrated: ")

    f = function(expr)

    dx, y = get_interval_points(n, f, intLimits)
    

    print(rectangular(dx, y))