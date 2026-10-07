class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d1={"}":"{",")":"(","]":"["}
        for ch in s:
            if ch in"({[":
                st.append(ch)
            else:
                if st==[] or st[-1]!=d1[ch]:
                    return False
                st.pop()
        return st==[]