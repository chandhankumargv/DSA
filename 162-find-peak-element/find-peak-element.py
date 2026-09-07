class Solution(object):
    def findPeakElement(self, nums):
        max = 0
        s = 0
        e = len(nums)-1
        while s<e:
            if nums[s]>nums[e]:
                max = s
                e -= 1
            else:
                max = e
                s += 1
        return max
        