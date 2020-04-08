"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?"""

"""ACCEPTED__----
class Solution(object):
    def singleNumber(self, nums):
        self.nums=nums
        s_sum=0
        s=0
        k=set()
        
        for i in range(len(nums)):
            k.add(nums[i])
            s=s+nums[i]
            
        k=list(k)
        
        for i in range(len(k)):
            s_sum=s_sum+k[i]
        return (2*s_sum-s)
        
         
   ""from collections import Counter
arr=[2,2,5,9,9,2,5,1,1]
x=0
k=Counter(arr)
print(k.get(9))
print(type(k[1]))
for i in k:
    if k.get(i)!=2:
        print(i)

for i in arr:
    x=x^i

print(x)

"""