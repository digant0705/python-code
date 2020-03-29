dic=dict()
arr=[5,4,7,8,4,8,8,3,7,7,6,3,7,6,5,6,8,4,5,7,4,7,7,5,2,5,6,6,8,1,6,8,8,8,9,3,2,9]
#d[key]=value

new_max=-1


for i in arr:
    dic[i]=dic.get(i,0)+1
print(dic)

for i in arr:
    if dic[i]==i and i > new_max:
        new_max=i
        
   
print(new_max)   

"""Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.


class Solution(object):
    def findLucky(self, arr):
        dic=dict()
        max=-1
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in arr:
            if dic.get(i)==i and i>max:
                max=i
        return max
                
                """