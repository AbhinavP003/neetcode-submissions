class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = {}
        has_duplicate = False
        for index, num in enumerate(nums):
            if num not in duplicateMap:
                duplicateMap[num] = index
            else:
                has_duplicate = True
                break
        return has_duplicate
                
        