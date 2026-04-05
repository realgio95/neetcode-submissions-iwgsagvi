class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # traverse string s in strs
        # if s is anagram of sorted str in kv
        # # add to dict at key anyways
        # res  = [] 
        # kv = {} # cat, act
        # cnts = Counter(strs)
        # for s in strs:
        #     if
        # for k,v in kv.items():
        #     res.append(v)
        # return res


        res  = [] 
        kv = {} # cat, act
        for s in strs:
            key = str(sorted(s))
            if key in kv:
                kv[key].append(s)
            else:
                kv[key] = []
                kv[key].append(s)
        for k,v in kv.items():
            res.append(v)
        return res