class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=0
        for i in candies:
            m = max(m,i)
            
        res = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                res[i]=True
            else:
                res[i]=False
        return res