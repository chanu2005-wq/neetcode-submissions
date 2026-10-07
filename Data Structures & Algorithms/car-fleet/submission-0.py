class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=sorted(zip(position,speed),key=lambda x: -x[0])
        st=[]
        for pos,std in car:
            time=(target-pos)/std

            if not st or time > st[-1]:
                st.append(time)

        return len(st) 