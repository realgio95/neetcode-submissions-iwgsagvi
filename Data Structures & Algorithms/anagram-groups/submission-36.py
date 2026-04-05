from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res  = [] 
        kv = defaultdict(list) # cat, act
        for s in strs:
            key = str(sorted(s))
            kv[key].append(s)
        for k,v in kv.items():
            res.append(v)
        return res