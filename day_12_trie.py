words=["digant","ashita","digree","arushi","arshita","distance","arunabh","ashima","nikhil","shagun","shasha"]
# Implementing a dictionary using trie data structure
_notExist="_notExist"
class Trie:
    
    def __init__(self):
        self._trie={}

    def insert(self,word):
        # this will insert words in the trie ds
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char]={}
            trie=trie[char]
        trie[_notExist]=_notExist

    def search_word(self,word):
        # this will search the given word and return T and F
        trie=self._trie
        for char in word:
            if char in trie:
                trie=trie[char]
            else:
                return False
        return trie.setdefault("_notExist",False)==_notExist
    
    def search_prefix(self,pre):
        # this will search the prefix nad return t/f accordingly
        trie=self._trie
        if pre =="":
            return True
        for pre in pre:
            if  pre in trie:
                trie=trie[pre]
            else:
                return False
        return True
    
    def print_words(self,pre):
        # this will print all the words starting with prefix
        trie=self._trie
        if pre =="":
            return True
        for pre in pre:
            if pre in trie:
                trie=trie[pre]
            else:
                return False
        return self.helper(trie)
    
    def helper(self,trie):
        l=[]
        for k,v in trie.items():
            if k==_notExist:
                subresult=[""]
            else:
                subresult=[k+s for s in self.helper(v)]
            l.extend(subresult)
        return l
           
                
trie = Trie()
for word in words:
    trie.insert(word)

def autoComplete(pre):
    all=[]
    auto=trie.print_words(pre)
    for i in auto:
        all.append(pre+i)
    print(all)    
    #"return [s + w for w in suffixes]"
    

print(trie.search_word("ashita"))
print(trie.search_prefix("aigant"))
autoComplete("a")




