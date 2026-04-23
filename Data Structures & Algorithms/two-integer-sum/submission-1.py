class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        popped = 0
        while nums != []:
            curr = nums.pop(0)
            popped += 1
            if target - curr in nums:
                return [i, nums.index(target-curr) + popped]
            i += 1

        