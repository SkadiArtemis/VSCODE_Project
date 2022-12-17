class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 4:
            if x == 0:
                return 0
            else:
                return 1
        else:
            l = 2
            r = x // 2
            while r - l > 1:
                m = (l + r) // 2
                m2 = m * m
                if m2 == x:
                    return m
                elif m2 > x:
                    r = m
                else:
                    l = m
            r2 = r * r
            if x == r2:
                return r
            else:
                return l