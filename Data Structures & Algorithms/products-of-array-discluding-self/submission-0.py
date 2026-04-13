class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        final_nums=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if j!=i:
                    prod*=nums[j]
            final_nums.append(prod)
        return final_nums