"""Given an array of integers, 
find the first missing positive integer in linear time and constant space.
 In other words, find the lowest positive integer that does not exist in the array.
 The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3
You can modify the input array in-place.
"""
#lets take a 5 element array n=5
arr=[1,6,4,5,6,2,3]
l=len(arr)
for i in range(len(arr)):
    if 0<int(arr[i]) and int(arr[i])<=len(arr):
        if type(arr[i]) is not str:
            if(arr[i]==len(arr)):
                print(arr[i])
                arr[0]=str(arr[0])
            else:
                if(type(arr[arr[i]]) is str):
                    {}
                else:
                    arr[arr[i]]=str(arr[arr[i]])
        
        else:
            arr[i]=int(arr[i])
            if(arr[i]==len(arr)):
                 arr[0]=str(arr[0])
                 arr[i]=str(arr[i])
            else:
                if(type(arr[arr[i]]) is str):
                  {}  
                else:
                    arr[arr[i]]=str(arr[arr[i]])
                    arr[i]=str(arr[i])
    else:
        {print(f"except->{arr[i]}")}
print(arr)

for i in range(l):
     if i==l-1:
         if type(arr[0]) is str:
             print(l+1)
     else:
    
         if type(arr[i+1]) is str:
             {}
         else:
            print(i+1)
            break



           
