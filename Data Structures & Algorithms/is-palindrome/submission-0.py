class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''.join(char for char in s if char.isalnum()).lower()
        
        i = 0
        j = len(newString) - 1
        while i < j:
            if newString[i] != newString[j]:
                return False
            i += 1
            j -= 1
        return True
