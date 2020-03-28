str="aaabb"
n=20
k=100
p1=n-2
p2=n-1
for i in range(k):
    
    if i:
        if p1==0 and p2==1:
            break
        elif p1+1==p2:
            p1=p1-1
            p2=n-1
        else:
            p2=p2-1
    print(p1+1,p2+1,i+1)
m=""        
for l in range(n):
        if l==p1+1 or l==p2+1:
            m=m+"b" 
        else:
            m=m+"a"
print(m) 
        
            
    
     