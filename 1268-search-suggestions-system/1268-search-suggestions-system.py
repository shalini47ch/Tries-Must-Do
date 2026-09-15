#here this is based on the concept of trie+collective dfs as here dfs performs the collection
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
    #now here create a helper function to perform dfs so that we can use 
    def dfs(self,node,path,res):
        if(len(res)==3):
            return 
        if node.isEnd():
            res.append(path)
        #traverse in alphabetical order
        for i in range(0,26):
            if(node.links[i]):
                #so here that character can be path
                self.dfs(node.links[i],path+chr(i+97),res)
    
    #here we will create a helper to perform get suggestions 
    def getSuggestions(self,trie,prefix):
        node=trie.root
        for ch in prefix:
            if not node.containsKey(ch):
                return []
            node=node.get(ch)
        res=[]
        self.dfs(node,prefix,res)
        return res

 
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie=Trie()
        #iterate through products and insert in trie
        for ele in products:
            trie.insert(ele)
        prefix=""
        ans=[]
        for ch in searchWord:
            prefix+=ch
            ans.append(self.getSuggestions(trie,prefix))
        return ans
        
        

       