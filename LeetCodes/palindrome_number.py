class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        l = len(z)
        i = 0
        while i <= l//2:
            if (z[i] != z[l-1-i]):
                return False
            i += 1
        return True
