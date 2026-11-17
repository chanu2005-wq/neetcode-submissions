class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for c in s:
            if '0'<=c<='9':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
