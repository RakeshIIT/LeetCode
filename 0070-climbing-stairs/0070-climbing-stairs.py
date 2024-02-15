class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==1:
        #     return 1
        # elif n==2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        ans = [0 for x in range(n+1)]
        ans[0],ans[1] = 1,1
        
        if n<=1:
            return n
        
        for i in range(2,n+1):
            ans[i] = ans[i-1]+ans[i-2]
            
        return ans[n]
        