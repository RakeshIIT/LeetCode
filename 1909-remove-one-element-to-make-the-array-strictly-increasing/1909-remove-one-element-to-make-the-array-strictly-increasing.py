class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        rem=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                rem+=1
                if i>1 and nums[i]<=nums[i-2]:
                    nums[i]=nums[i-1]    
        return rem<2
        