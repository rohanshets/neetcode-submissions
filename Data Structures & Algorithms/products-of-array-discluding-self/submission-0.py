class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            l.append(1)

        for j in range(len(nums)):
            for x in range(len(l)):
                if x != j:
                    l[x] *= nums[j]

        return l
