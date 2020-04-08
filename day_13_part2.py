X=[1,3,5]
def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    print("--",cache[4])
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache
print(staircase(5,X))

i=5
c=[0]*6
c[0]=1

for i in range(1,6):
    s=0
    for x in X:
        if i-x>=0:
            s+=c[i-x]
    c[i]=s    
            
    c[i]=s
print(c)