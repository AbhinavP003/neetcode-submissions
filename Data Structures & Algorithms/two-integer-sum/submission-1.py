class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        target_indexes = []
        target_dict[nums[0]] = 0
        for idx, num in enumerate(nums[1:], start=1):
            required_digit = target - num
            if required_digit in target_dict:
                target_indexes.append(target_dict[required_digit])
                target_indexes.append(idx)
                break
            else:
                target_dict[num] = idx
        return target_indexes