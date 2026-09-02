class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = list(s)
        lst_t = list(t)

        if sorted(lst_s) == sorted(lst_t):
            return True
        return False