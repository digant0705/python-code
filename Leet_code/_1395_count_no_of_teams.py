"""There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams)."""

def count_teams(arr):
    count=0
    for i in range(len(arr)):
        
        for j in range(i+1,len(arr)):
            
            for k in range(j+1,len(arr)):
                if arr[i]<arr[j]<arr[k] or arr[i]>arr[j]>arr[k]:
                   print(arr[i],arr[j],arr[k])
                   count+=1
    
    return count

arr=[3,6,7,5,1]
print(count_teams(arr))
