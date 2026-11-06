class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for l in logs:
            if l=="../":
                if st:
                    st.pop()
            elif l!="./":
                st.append(l)
        return len(st)