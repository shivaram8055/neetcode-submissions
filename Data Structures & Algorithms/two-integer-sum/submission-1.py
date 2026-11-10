class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict ={}
        for i in range(len(nums)):
            d=target-nums[i]
            if d in sum_dict:
                return [sum_dict[d],i]
            sum_dict[nums[i]]=i