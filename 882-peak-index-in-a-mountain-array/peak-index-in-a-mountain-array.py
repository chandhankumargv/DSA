class Solution(object):
    def peakIndexInMountainArray(self, arr):
        s = 0
        e = len(arr) - 1
        
        while s < e:
            m = s + (e - s) // 2
            if arr[m] < arr[m + 1]:
                s = m + 1
            else:
                e = m
        return s
