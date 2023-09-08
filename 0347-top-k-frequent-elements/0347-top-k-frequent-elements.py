class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref={}
        li=[[] for i in range(len(nums))]
        ans=[]
        for i in nums:
            ref[i]=ref.get(i,0)+1
        for num, rep in ref.items():
            li[rep-1].append(num)
        newli = li[::-1]
        for a in newli:
            for b in a:
                ans.append(b)
                if len(ans)==k:
                    return ans
                



