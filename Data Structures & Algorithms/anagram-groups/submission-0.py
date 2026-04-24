class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        newLst = []
        i = 0
        j = 0
        curr = strs.pop(0)
        newLst.append([curr])
        while strs != []:
            if i >= len(strs):
                i = 0
                curr = strs.pop(0)
                newLst.append([curr])
                if strs == []:
                    break
                j += 1
            if Counter(curr) == Counter(strs[i]):
                newLst[j].append(strs.pop(i))
            else:
                i+=1
        return newLst
        
            
