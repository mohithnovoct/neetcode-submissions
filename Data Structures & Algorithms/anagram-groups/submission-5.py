class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            srts = ''.join(sorted(s))
            res[srts].append(s)
        return list(res.values())