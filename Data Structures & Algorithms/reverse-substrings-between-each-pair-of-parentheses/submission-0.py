class Solution:
    def reverseParentheses(self, s: str) -> str:
        p=[0]*len(s)
        st=[]
        for i,c in enumerate(s):
            if c=="(": st.append(i)
            elif c==")":
                j=st.pop()
                p[i],p[j]=j,i
        ans=[]
        i,d=0,1
        while i<len(s):
            if s[i] in "()":
                i=p[i]
                d=-d
            else:ans.append(s[i])
            i+=d
        return "".join(ans)
