class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        s1 = n*(n+1)//2
        s2 = sum(nums)

        act_unique = sum(set(nums))
        dup = s2 - act_unique
        real = s1 - act_unique
        return dup,real
            