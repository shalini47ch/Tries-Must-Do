#lets use the concept of trie+dfs and one more parameter self.word to store the word at the end 
class Node:
    def __init__(self):
        self.links=[None for i in range(26)]
        self.flag=False 
        self.word=None 
    
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
        node.word=word 

class Solution:
    def dfs(self,board,r,c,node,res):
        if(r<0 or r>=len(board)):
            return 
        if(c<0 or c>=len(board[0])):
            return 
        if(board[r][c]=="#"):
            return  
        ch=board[r][c]
        if not node.containsKey(ch):
            return 
        node=node.get(ch)
        #means complete word found
        if(node.isEnd()):
            res.append(node.word)
            node.flag=False
        board[r][c]="#"
        #now explore directions
        self.dfs(board,r-1,c,node,res)
        self.dfs(board,r+1,c,node,res)
        self.dfs(board,r,c-1,node,res)
        self.dfs(board,r,c+1,node,res)
        #now undo the board[r][c]
        board[r][c]=ch

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie=Trie()
        #insert all the words in the trie
        for word in words:
            trie.insert(word)
        res=[]
        #traverse through the board
        n=len(board)
        m=len(board[0])
        for r in range(0,n):
            for c in range(0,m):
                self.dfs(board,r,c,trie.root,res)
        return res
        