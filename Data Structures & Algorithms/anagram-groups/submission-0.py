class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            srt = ''.join(sorted(s))
            res[srt].append(s)
        return list(res.values())