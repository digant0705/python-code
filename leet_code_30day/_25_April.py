class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return 1
        
        def possible(arr,ind):
            if arr[ind]==0:
                return -1
            for i in range(arr[ind],0,-1):
                if arr[ind]>=len(nums)-1-ind:
                    return 1
                else:
                    if possible(arr,ind+i)==1:
                        return 1
        return possible(nums,0)==1   
        
    def canJump(self, nums: List[int]) -> bool:
        check=[0]*len(nums)
        if len(nums)==1:
            return 1
        
        def possible(arr,ind):
            
            if arr[ind]==0:
                return 0
            elif arr[ind]>=(len(arr)-1-ind):
                return 1
            else:
                
                for j in range(arr[ind],0,-1):
                    if check[ind+j]:
                        return 1
                return 0
        
        for i in range(len(nums)-1,-1,-1):
        
            check[i]=possible(nums,i)
            
        
        return check[0]
        