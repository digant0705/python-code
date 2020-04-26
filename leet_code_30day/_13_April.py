"one of the beautiful question of leet code--"
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_l=0
        h={}
        h[0]=-1
        count=0
        for i,j in enumerate(nums):
            if j:
                count+=1
            else:
                count-=1
                
            
            if count in h:
                max_l=max(max_l,i-h[count])
            else:    
                h[count]=i
            
        return max_l
                    
                    
                    
                    
                
        
        
           
            
        

            
        