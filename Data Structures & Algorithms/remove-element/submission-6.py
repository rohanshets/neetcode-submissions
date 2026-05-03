class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        if val not in nums:
            return len(nums)
        nums.sort()
        i = nums.index(val)
        j = i
        while j < i + nums.count(val):
            print(nums)
            nums.append(nums.pop(nums.index(val)))
            j += 1
        return nums.index(val)
        