class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for c in s:
            if st and (st[-1],c) in [('A','B'),('C','D')]:
                st.pop()
            else:
                st.append(c)
        return len(st)
