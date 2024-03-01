class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l=0
        r=l+1
        while r<len(prices):
            if prices[r]>prices[l]:
                max_prof=max(max_prof,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return max_prof