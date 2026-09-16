#we need to find the shortest word and then replace it
#use the concept of tries to solve this 
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
    
    #now create a helper function to replace the word
    def replaceWord(self,word):
        node=self.root
        prefix=""
        for i in range(0,len(word)):
            if node.isEnd():
                return prefix 
            if not node.containsKey(word[i]):
                return word 
            prefix+=word[i]
            node=node.get(word[i])
        if(node.isEnd()):
            return prefix 
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #insert the words of the dictionary in trie
        trie=Trie()
        #traverse through dictionary and put the words in dictionary
        for word in dictionary:
            trie.insert(word)
        words=sentence.split()
        res=[]
        for word in words:
            res.append(trie.replaceWord(word))
        return " ".join(res)


        