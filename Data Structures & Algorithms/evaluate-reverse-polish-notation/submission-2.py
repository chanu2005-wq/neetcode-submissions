class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            match token:
                case "+":
                    st.append(st.pop()+st.pop())
                case "-":
                    b,a=st.pop(),st.pop()
                    st.append(a-b)
                case "*":
                    st.append(st.pop()*st.pop())
                case "/":
                    b,a=st.pop(),st.pop()
                    st.append(int(a/b))
                case _:
                    st.append(int(token))
        return st[-1]