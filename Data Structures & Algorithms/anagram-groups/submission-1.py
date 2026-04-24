class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #have this
        out = []
        catalog = {}

        for s in strs:
            flag = 0
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            # print(s, out)
            for i in range(len(out)):
                if catalog[i] == d:
                    out[i].append(s)
                    flag = 1
                    break
            
            if flag == 0:
                out.append([s])
                catalog[len(out) - 1] = d
            
        return out
            

            
            


        #go thorugh every single string, convert it into a dictionary
            #then for every single item in out, see if they fit into one of these groups. if not, add a new group.
        




        