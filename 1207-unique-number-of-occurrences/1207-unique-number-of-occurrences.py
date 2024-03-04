class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ref ={}
        for i in arr:
            ref[i]=ref.get(i,0)+1
            
        return len(ref.values()) == len(set(ref.values()))
        