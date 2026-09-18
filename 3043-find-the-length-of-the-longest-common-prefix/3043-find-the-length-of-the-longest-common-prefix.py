#lets use the concept of tries to solve this 
class Node:
    def __init__(self):
        #here we have numbers instead of characters so take care of those
        self.links=[None for i in range(10)]
        self.flag=False 
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord("0")]!=None 
    
    def put(self,ch):
        self.links[ord(ch)-ord("0")]=Node()
    
    def get(self,ch):
        return self.links[ord(ch)-ord("0")]
    
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
    
    #create one for helper for startsWith
    def startsWith(self,prefix):
        node=self.root
        count=0
        #since we need the length here we will use count 
        for i in range(0,len(prefix)):
            if not node.containsKey(prefix[i]):
                return count 
            node=node.get(prefix[i])
            count+=1
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #here we put the elements of arr2 in trie
        trie=Trie()
        maxi=0
        for i in range(0,len(arr2)):
            trie.insert(str(arr2[i]))
        for i in range(0,len(arr1)):
            temp=trie.startsWith(str(arr1[i]))
            #here we need to return the length of longest common prefix
            maxi=max(maxi,temp)
        return maxi

        