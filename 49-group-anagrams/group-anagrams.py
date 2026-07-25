class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping=defaultdict(list)
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            mapping[tuple(count)].append(s)
        return list(mapping.values())