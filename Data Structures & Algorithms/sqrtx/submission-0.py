class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        ans=-1
        while l<=r:
            m=(l+r)//2
            msq=m*m

            if msq==x:
                return m
            elif msq>x:
                r=m-1
            else:
                ans=m
                l=m+1
        return ans