"Happy number"


seen=set()
def sum_square_digit(n):
    sum_square=0
    while(n):
        sum_square+=int(n%10)*int(n%10)
        n=int(n/10)
    return sum_square

def check_happy_number(n):
    
    k=sum_square_digit(n)
    if 1==k:
        return True
    elif k not in seen:
        seen.add(k)
    else:
        return False
    return check_happy_number(k)
    

print(check_happy_number(68))
       

