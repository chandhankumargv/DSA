class Solution(object):
    def peakIndexInMountainArray(self, arr):
        s = 0
        m = 0
        e = len(arr)-1
        while s < e:
            if arr[s]>arr[e]:
                e -= 1
                m = s
            else:
                s += 1
                m = e
        return m
        