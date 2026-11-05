class Solution:
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)
        while l+1<r and s[l]==s[r-1]:
            c=s[l]
            while l<r and s[l]==c:
                l+=1
            while l<r and s[r-1]==c:
                r-=1
        return r-l

