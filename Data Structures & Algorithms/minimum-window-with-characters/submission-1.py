from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need=Counter(t)
        wi={}
        have=0
        need_count=len(need)
        res=[-1,-1]
        res_len=float("inf")
        left=0
        for right in range(len(s)):
            ch=s[right]
            wi[ch]=wi.get(ch,0)+1
            if ch in need and wi[ch]==need[ch]:
                have+=1
            while have==need_count:
                if (right-left+1)<res_len:
                    res=[left,right]
                    res_len=right-left+1
                wi[s[left]]-=1
                if s[left] in need and wi[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if res_len!=float("inf") else ""
