#here we need to return the maximum result of nums[i] xor nums[j]
class Node:
    def __init__(self):
        self.links=[None,None]
    
    def containsKey(self,bit):
        return self.links[bit]!=None 
    
    def put(self,bit):
        self.links[bit]=Node()
    
    def get(self,bit):
        return self.links[bit]

#now create a helper for trie
class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,num):
        #here we need to iterate from 31 till 0
        node=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if not node.containsKey(bit):
                node.put(bit)
            node=node.get(bit)
    
    #now create a helper to find the maximum
    def getMax(self,num):
        node=self.root
        ans=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            opposite=1-bit 
            if node.containsKey(opposite):
                ans=ans|(1<<i)
                node=node.get(opposite)
            else:
                node=node.get(bit)
        return ans
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        #here we will store bits instead of characters 
        trie=Trie()
        for num in nums:
            trie.insert(num)
        maxi=0
        #now we need to find maximum xor 
        for num in nums:
            maxi=max(maxi,trie.getMax(num))
        return maxi

        
        