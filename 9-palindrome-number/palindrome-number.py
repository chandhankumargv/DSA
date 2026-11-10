class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
            
        # Convert the integer to a string
        s = str(x)
        n = len(s)
        
        # Check characters up to the middle of the string
        for i in range(n // 2):
            # Compare the character from the front with the character from the back
            if s[i] != s[n - 1 - i]:
                return False
                
        return True
