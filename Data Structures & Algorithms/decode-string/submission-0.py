class Solution:
    def decodeString(self, s: str) -> str:
        st_st=[]
        co_st=[]
        cur=""
        k=0

        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                st_st.append(cur)
                co_st.append(k)
                cur=""
                k=0
            elif c=="]":
                temp=cur
                cur=st_st.pop()
                count=co_st.pop()
                cur+=temp*count
            else:
                cur+=c
        return cur