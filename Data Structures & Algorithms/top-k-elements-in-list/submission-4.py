class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1
        print(frequency_dict)
        grouped_list = []
        for key,v in frequency_dict.items():
            grouped_list.append((key,v))
        print(grouped_list)
        grouped_list.sort(key=lambda x: x[1])
        print(grouped_list)
        return_list = []
        for tup in grouped_list[-k:]:
            return_list.append(tup[0])
        return return_list