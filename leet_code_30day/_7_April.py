#counted array element as x to x+1 in array .count total such elemensts
from collections import Counter
arr=[1,1,3,3,5,8,5,7,7]

def f(arr):
    count=0
    a=Counter(arr)
    print(a)
    for x in a:
        if x+1 in a:
            count=count+a[x]
    print(count)
        
def g(arr):
    return sum([1 for x in arr if x+1 in arr])

    
print(g(arr))
