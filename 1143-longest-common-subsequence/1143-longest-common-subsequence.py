class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #use the concept of recursion+memo to solve this 
        m=len(text1)
        n=len(text2)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.helper(m-1,n-1,text1,text2,m,n,dp)

    def helper(self,ind1,ind2,s1,s2,m,n,dp):
        if(ind1<0 or ind2<0):
            return 0
        if(dp[ind1][ind2]!=-1):
            return dp[ind1][ind2]
        if(s1[ind1]==s2[ind2]):
            dp[ind1][ind2]=1+self.helper(ind1-1,ind2-1,s1,s2,m,n,dp)
            return dp[ind1][ind2]
        else:
            ele1=self.helper(ind1-1,ind2,s1,s2,m,n,dp)
            ele2=self.helper(ind1,ind2-1,s1,s2,m,n,dp)
            dp[ind1][ind2]=max(ele1,ele2)
            return dp[ind1][ind2]
      