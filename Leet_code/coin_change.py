#we have coins of 1,2,5,10 find the min coins required
arr=[1,2,5,10]
def f(x,arr):
    arr=sorted(arr,reverse=True)
    s=0
    for i in arr:
        
        s=s+ int(x/i)
        print(s)
        if x%i==0:
            
            return int(s)
        else:
            x=x%i
print(f(57,arr)) 

#now arr=[25,10,1] for 31 ---> 4 not 7
coin=[1,10,25]
def g(x,coin):
    if x<0:
        return -1
    dp=[x]*(x+1)
    print(dp)
    dp[0]=0
    for i in coin:
        for j in range(x+1):
            if i<=j:
               dp[j]=min(dp[j],1+dp[j-i])
    print(len(dp))
    return dp[x] if dp[x]<x else -1
print(g(31,coin))

    