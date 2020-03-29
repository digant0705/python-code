arr=[2,2,2,4]
check=[0,0,0,0,0]

for i in arr:
    check[abs(i)]=check[abs(i)]+1

print(check)