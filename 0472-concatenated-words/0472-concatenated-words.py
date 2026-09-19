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
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        #we need to make sure that the shorter words be inserted first
        words.sort(key=len)
        trie=Trie()
        res=[]
        for word in words:
            n=len(word)
            dp=[False for i in range(n+1)]
            dp[0]=True 
            for i in range(0,n):
                if not dp[i]:
                    continue
                node=trie.root
                #now iterate from j till n
                for j in range(i,n):
                    ch=word[j]
                    if not node.containsKey(ch):
                        break
                    node=node.get(ch)
                    if(node.isEnd()):
                        dp[j+1]=True
            if(dp[n]):
                res.append(word)
            trie.insert(word)
        return res


        