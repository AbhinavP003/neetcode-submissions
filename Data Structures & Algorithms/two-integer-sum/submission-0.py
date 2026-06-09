class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complemet_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complemet_map.get(complement)!= None:
                return [complemet_map[complement], index]
            else:
                complemet_map[num] = index
        return []