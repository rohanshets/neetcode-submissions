class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            if i == "":
                encoded += "\n"
            else:
                encoded += i
                encoded += "\n"
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s[:len(s)-1].split("\n")
