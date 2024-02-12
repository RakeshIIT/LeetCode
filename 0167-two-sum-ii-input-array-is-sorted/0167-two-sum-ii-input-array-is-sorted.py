class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ref={}
        ans=[]
        for i in range(len(numbers)):
            if (target - numbers[i]) in ref:
                ans.append(ref[target-numbers[i]]+1) 
                ans.append(i+1) 
                break
            else:
                ref[numbers[i]] = i
        return ans