class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res=x
        ix,inn=1,1
        while inn<=n-1:
            if ix&x==0:
                if inn&(n-1):
                    res=res|ix
                inn=inn<<1
            ix=ix<<1
        return res