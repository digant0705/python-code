""" plus 1"""

from collections import Counter
s=""
arr=[9,9,9,9]
ar=[]
for i in range(len(arr)):
    s=s+str(arr[i])
print(int(s)+1)

k=int(s)+1
k=str(k)
for i in range(len(k)):
    ar.append(int(k[i]))
print(ar)