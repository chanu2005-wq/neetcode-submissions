class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res=[]
        for text in (s,t):
            st=[]
            for c in text:
                if c=="#":
                    if st:st.pop()
                else:st.append(c)
            res.append(st)
        return res[0]==res[1]
