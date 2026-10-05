class Solution(object):
    def firstUniqChar(self, s):
        counts = Counter(s)  # Automatically does Pass 1
        
        for index, char in enumerate(s):  # Pass 2
            if counts[char] == 1:
                return index
        return -1
