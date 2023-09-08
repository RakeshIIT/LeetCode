class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref=defaultdict(list)
        for w in strs:
            li=[0]*26
            for c in w:
                li[ord(c)-ord('a')]+=1
            ref[tuple(li)].append(w)
        return ref.values()
