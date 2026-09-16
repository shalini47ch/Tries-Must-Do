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


#now similarly do for Trie
class Trie:
    def __init__(self):
        self.root=Node()
    
    #now create a helper function to perform the insert operation
    def insert(self,word):
        node=self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            node=node.get(word[i])
        node.setEnd()
    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        #we need to return the length of the longest word with the smallest lexicographical order lets use the concept of tries to solve this
        trie=Trie()
        #traverse through words and insert in the trie
        for word in words:
            trie.insert(word)
        ans=""
        for word in words:
            node=trie.root
            valid=True
            for ch in word:
                if not node.containsKey(ch):
                    valid=False
                    break
                node=node.get(ch)
                if not node.isEnd():
                    valid=False
                    break
            if valid:
                if(len(word)>len(ans)):
                    ans=word
                elif(len(word)==len(ans)):
                    ans=min(ans,word)
        return ans
        

        