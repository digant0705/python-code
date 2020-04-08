"maximum sub array sum"

arr=[2,1,7]
dp=[0]*len(arr)


print(dp)

def f(arr,ind):
    if ind==0: 
        print(ind,arr[ind]) 
        dp[ind]=arr[ind]  
        print("oth element",dp)
        
        return arr[ind]
    
    
    dp[ind]= max(arr[ind],arr[ind]+f(arr,ind-1))
    print(dp)
    dp[0]=max(dp[ind],dp[0])
    
    return dp[ind]
    

k=f(arr,len(arr)-1)
print(dp[0])

        

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest= -float("inf")
        current=0
        
        for num in nums:
            current+=num
            highest=max(current,highest)
            current=max(0,current)
        return highest
        """