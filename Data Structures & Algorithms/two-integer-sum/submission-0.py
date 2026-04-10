class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inds=[]
        for i in range(0,len(nums)-1):
            prev_ele=nums[i]
            for j in range(i+1,len(nums)):
                next_ele=nums[j]
                if prev_ele+next_ele==target:
                    inds.append(i)
                    inds.append(j)
                    return inds