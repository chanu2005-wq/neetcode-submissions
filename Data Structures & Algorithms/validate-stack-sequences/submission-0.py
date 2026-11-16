class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        st=[]
        for n in pushed:
            st.append(n)
            while i<len(popped) and st and popped[i]==st[-1]:
                st.pop()
                i+=1
        return not st