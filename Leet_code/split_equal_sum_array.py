#416 partition leet code --return t/f
#[1,5,5,11] return t
#[1,3,5] return f

arr=[100,100,100,100,100,100,100,100,100,100,100,100]
"""arr=[1,2,3,6]"""
def f(arr):
    total=sum(x for x in arr)
    if total%2==1:
        return False
    else:
        print(total)
        dp=[0]* (len(arr)+1)
        print(dp[0]==True)
        return g(arr,0,0,total,dp)
    
def g(arr,ind,total,gtotal,dp):
    if dp[ind] !=0:
        print("ind",ind)
        return dp[ind]
    
    if total==gtotal/2:
        dp[ind]=True
        return dp[ind] 
    elif total>gtotal/2 or ind>=len(arr):
        dp[ind]=False
        return dp[ind]
    else:
        dp[ind]= g(arr,ind+1,total,gtotal,dp) or g(arr,ind+1,total+arr[ind],gtotal,dp)

        return dp[ind]==True
print(f(arr))