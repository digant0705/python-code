
s=5
def fun1(k):
   global s
   s=s+k 
   print(s)
   return True

def fun2(l):
    global s
    s=s+l
    print(s)
print(fun1(2))
print(fun2(2))

print(1)
