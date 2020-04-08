# find the longest substring with k length
# abcba k=2 result bcb

def f(str,k):
    b=[] 
    if k>len(str):
        return -1   
    for i in range(len(str)):
        s=set()
        a=[]
        m=k
        for j in range(i,len(str)):   
            if str[j] not in s:
                m-=1
                if m<0:
                    break
                else:
                    s.add(str[j])
                    a.append(str[j])
            else:
                a.append(str[j])
        
       
        if len(a)>len(b):       
            b=a
    
    return "".join(b)

print(f("aWORLllllD",4))

             