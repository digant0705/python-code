"Anagram:"
from collections import defaultdict

def isAnagrams(a,b):

    #function to check if both are anagras or not and return T and F
    return sorted(a)==sorted(b)
def anagras_hash(a,b):

    #function to check anagram using dic  print(anagras_hash("ass","ass"))
    d={}
    for char in a:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1

    for char in b:
        if char in d:
            d[char]-=1
        else:
            d[char]=1
    for i in d:
        if d[i]!=0:
            return False
    
    return True


def f(words):
    #using default dic as-- h={key :[]}
    h=defaultdict(list)
    l=[]
    for word in words:
        h["".join(sorted(word))].append(word)
            
    for v in h.values():
        l.append(v)
    return l

def g(words):
    # usning setdefault
    h={}
    l=[]
    for word in words:
        h.setdefault("".join(sorted(word)),[]).append(word)
        
            
    for v in h.values():
        l.append(v)
    return l



words=["eat", "tea", "tan", "ate", "nat", "bat"]
print(g(words))



