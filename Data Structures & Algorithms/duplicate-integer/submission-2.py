class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        for i in cnt.values():
            if i!=1:
                return True
        return False

