# calculate pie using monte carlo method 
"area of cirle/area of square *4"

from random import uniform
from math import sqrt

def g(n):
    c=0
    for _ in range(n):
        x=uniform(0,1)
        y=uniform(0,1)
        if sqrt(x**2 + y**2) <1:
            c=c+1
        
    return (4*c/n)

print(g(10))