# 1,3,5 steps problem

def f(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    return f(n-1)+f(n-2)

def g(n):
    a,b =1,2
    for _ in range(n-1):
        a,b=b,a+b
    return a


def h(n):
    a,b=1,2
    if n<1:
        return 0
    elif n==1:
        return a
    elif n==2:
        return b
    for _ in range(n-2):
        b=a+b
        a=b-a
    return b

def d(n):
    dp=[0]*(n+1)
    if n<0:
        return 0
    elif n==0:
        dp[0]=1
        return dp[0]
    
    dp[n]= d(n-1)+d(n-2)
    return dp[n]

def l(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    dp[2]=2
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        print("here")
        for i in range(2,n):
            dp[i+1]=dp[i]+dp[i-1]
            print(dp[i+1])
    return dp[n]


#print(f(25))
#print(g(50))
#print(h(50))
#print(d(50))
print(l(10))




