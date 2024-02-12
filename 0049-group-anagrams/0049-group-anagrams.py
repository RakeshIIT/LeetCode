class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for word in strs:
            li=[0]*26
            for c in word:
                li[ord(c)-ord('a')]+=1
            if tuple(li) in ref:
                ref[tuple(li)].append(word)
            else:
                ref[tuple(li)] = [word]
        return ref.values()
