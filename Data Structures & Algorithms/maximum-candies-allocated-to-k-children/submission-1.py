class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l,h=0,max(candies)
        while l<h:
            m=(l+h+1)//2
            pos=sum(x//m for x in candies)
            if pos>=k:
                l=m
            else:
                h=m-1
        return l

