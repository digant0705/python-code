s="digant"

def f(s,ind):
    if ind==len(s):
        return
    f(s,ind+1)
    print(s[ind],end="")
f(s,0)
