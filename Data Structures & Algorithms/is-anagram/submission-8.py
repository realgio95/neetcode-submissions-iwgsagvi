class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s racecar
        # t carrace
        # go through the first one and add to a counter map variable like an array 
        cnts = [0] * 26

        if len(s) != len(t):
            return False

        for i in s:
            cnts[ord(i)-ord('a')]+=1

        for j in t:
            cnts[ord(j)-ord('a')]-=1

        for i in cnts:
            if (i > 0):
                return False
        return True
            
        # tips
            # use a dict instead
            # use Counter
            # ord - ord a