class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 0
        uniqueEle = dict(Counter(nums))
        res = 0
        for key, value in uniqueEle.items():
            if value >= maxCount:
                res = key
                maxCount = value

        return int(res)