class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for c in num:
            while k and st and st[-1]>c: st.pop(); k-=1
            st.append(c)
        if k: del st[-k:]
        return "".join(st).lstrip("0") or "0"
