class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        n=len(nums)
        while j<n:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        
        # res=[0]*len(nums)
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         print(nums[i],j)
        #         res[j]=nums[i]
        #         j+=1
        # print(res)
        