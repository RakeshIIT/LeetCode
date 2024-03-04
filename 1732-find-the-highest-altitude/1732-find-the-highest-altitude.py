class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        val=0
        for i in range(len(gain)):
            val+=gain[i]
            ans=max(ans,val)
        return ans
        