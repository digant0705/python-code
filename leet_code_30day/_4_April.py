"shift zeros without changing th relative position of array non zero elements"

arr=[0,1,0,3,12]

def f(a):
    for i in range(len(arr)):
        t=i
        for j in range(i+1,len(arr)):
            if a[t]==0:
                if a[j]!=0 :
                    k=a[t]
                    a[t]=a[j]
                    a[j]=k
                    t=j
                
                
                    
        
            
    print(a)
f(arr)


    



