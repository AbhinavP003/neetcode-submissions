import uuid
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        uid = str(uuid.uuid4())
        # len of uid is 36
        return uid.join(strs) + uid 

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        uid = s[-36:]
        s = s[:-36]

        return s.split(uid)