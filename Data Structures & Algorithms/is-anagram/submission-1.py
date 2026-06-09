class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string_map = {}
        for char in s:
            if char in string_map:
                string_map[char]+=1
            else:
                string_map[char] = 1

        for char in t:
            if char in string_map and string_map[char] > 0:
                string_map[char]-=1
            else:
                return False
        return True


        