class Solution:
    def reverse(self, x: int) -> int:
        max_in = 2**31 - 1
        min_in = -2**31
        rev = str(x)
        
        if x < 0:
            reversed= "-"+rev[1:][::-1]
        else:
            reversed= rev[::-1]
        result = int(reversed)

        if result < min_in or result > max_in:
            return 0
        return result
        