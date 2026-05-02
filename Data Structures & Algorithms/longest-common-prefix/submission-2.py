class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<2:
            return strs[0] or ""
        i = 0
        curr = ""
        prev = ""
        string = ""
        l = []
        for j in strs:
            l.append(list(j))
        while i < len(strs):
            if i==0:
                try:
                    prev = l[i].pop(0)
                except:
                    return string
            else:
                try:
                    curr = l[i].pop(0)
                except:
                    return string
                if curr == prev:
                    prev = curr
                else:
                    return string
            i+=1
            if i==len(strs):
                string += curr
                i = 0