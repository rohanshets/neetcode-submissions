class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]*len(nums)
        backward = [1]*len(nums)
        for x in range(len(nums)):
            if x == 0:
                forward[x] = 1
            else:
                forward[x] = forward[x-1]*nums[x-1]
        for x in range(len(nums)-1, -1, -1):
            if x == len(nums)-1:
                backward[x] = 1
            else:
                backward[x] = backward[x+1]*nums[x+1]
        result = []
        print(backward, forward)
        for x in range(len(nums)):
            result.append(backward[x]*forward[x])
        return result
