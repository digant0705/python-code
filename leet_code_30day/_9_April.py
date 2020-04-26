#string --> #is treated as backslash ie backspace 
# a#b#c ==a#c -->  c==c true

def f(s1,s2):
    s3=""
    s4=""
    for i in s1:
        s3=s3+i
        if i=="#":
            s3=s3[:len(s3)-2]
    for i in s2:
        s4=s4+i   
        if i=="#":
            s4=s4[:len(s4)-2]
    return s3==s4



print(f("ab#c","ad#c"))