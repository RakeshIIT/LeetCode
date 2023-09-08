class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        pref=1
        for i in range(len(nums)):
            ans[i]=pref
            pref*=nums[i]
        post=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]=ans[j]*post #only change here is we multiply with postfix --> this will prevent overwriting
            post*=nums[j]
        return ans

