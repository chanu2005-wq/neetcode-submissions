class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st,k=[],float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<k:
                return True
            
            while st and st[-1]<nums[i]:
                k=st.pop()
            st.append(nums[i])
        return False
