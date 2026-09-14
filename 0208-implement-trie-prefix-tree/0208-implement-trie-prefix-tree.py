#first create a node and then perform the functions accordingly
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
        
    def insert(self, word: str) -> None:
        node=self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            node=node.get(word[i])
        node.setEnd()

    def search(self, word: str) -> bool:
        node=self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return False 
            node=node.get(word[i])
        return node.isEnd()
        
    def startsWith(self, prefix: str) -> bool:
        #here we need to return True or False
        node=self.root
        for i in range(0,len(prefix)):
            if not node.containsKey(prefix[i]):
                return False
            node=node.get(prefix[i])
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)