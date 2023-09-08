class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        se=set(nums)
        for i in nums:
            if i-1 not in se:
                length=0
                while i+length in se:
                    length+=1
                longest=max(length, longest)
        return longest