class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(string)
            else:
                anagram_dict[sorted_str] = [string]

        return list(anagram_dict.values())
        