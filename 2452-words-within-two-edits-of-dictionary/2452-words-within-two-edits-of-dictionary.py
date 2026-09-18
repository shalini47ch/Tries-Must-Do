#this is based on the concept of trie+dfs 
class Node:
    def __init__(self):
        self.links=[None for i in range(26)]
        self.flag=False 
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord("a")]!=None 
    
    def put(self,ch):
        self.links[ord(ch)-ord("a")]=Node()
    
    def get(self,ch):
        return self.links[ord(ch)-ord("a")]
        
    def setEnd(self):
        self.flag=True 
    
    def isEnd(self):
        return self.flag

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,word):
        node=self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            node=node.get(word[i])
        node.setEnd()

    
class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        #first lets insert the words of the dictionary in tries and then perform dfs with all 26 characters with the condition that it should be end of word and mismatch<=2 means the edits shouldnt be more
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        #now the next step is to perform dfs 
        def dfs(node,word,ind,mismatch):
            if(mismatch>2):
                return False
            if(ind==len(word)):
                #means poora iterate hogaya hai
                return node.isEnd() and mismatch<=2
            indi=ord(word[ind])-ord("a")
            for ch in range(0,26):
                child=node.links[ch]
                if child:
                    if(ch==indi):
                        #means that character already exists so there is no need to edit
                        if(dfs(child,word,ind+1,mismatch)):
                            return True
                    else:
                        #here characters are not same so edits are needed
                        if(dfs(child,word,ind+1,mismatch+1)):
                            return True
            return False
        #now at last we need the words 
        res=[]
        for q in queries:
            if(dfs(trie.root,q,0,0)):
                res.append(q)
        return res
                


        