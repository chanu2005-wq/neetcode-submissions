class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        paths=path.split("/")

        for c in paths:
            if c=="..":
                if st:
                    st.pop()
            elif c!="" and c!=".":
                st.append(c)
        return "/"+"/".join(st)