class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_pdt = 1
        is_zero_present = False
        zero_indexes = []
        for idx, num in enumerate(nums):
            if num == 0:
                zero_indexes.append(idx)
                is_zero_present = True
                continue
            
            total_pdt = total_pdt * num
        
        return_list = []
        if is_zero_present:
            if len(zero_indexes) == 1:
                for i in range(len(nums)):
                    if i == zero_indexes[0]:
                        return_list.append(total_pdt)
                    else:
                        return_list.append(0)
            else:
                for i in range(len(nums)):
                    return_list.append(0)
        else:
            for i in range(len(nums)):
                return_list.append(total_pdt//nums[i])

        return return_list