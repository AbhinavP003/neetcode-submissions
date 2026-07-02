class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            anagram_dict[sorted_str].append(string)

        return list(anagram_dict.values())
        