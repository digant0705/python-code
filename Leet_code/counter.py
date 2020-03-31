from collections import Counter

arr=[1,1,1,1,5,6,7,5,5,6,5,5,9]
print(Counter(arr)[1])
print(sorted(Counter(arr),reverse=True))
for x in sorted(Counter(arr), reverse=True):
            if Counter(arr)[x] == x:
                print(x)
print(-1)
