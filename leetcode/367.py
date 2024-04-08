class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        cmp = num**(1/2) - int(num**(1/2))
        if cmp > 0:
            return False
        else:
            return True