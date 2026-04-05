class Solution:
    def isAnagram(self, s: str, t: str):
        # s racecar
        # t carrace
        # go through the first one and add to a counter map variable like an array 
        cnts = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            cnts[ord(s[i])-ord('a')]+=1

        for j in range(0, len(t)):
            cnts[ord(t[j])-ord('a')]-=1

        for i in cnts:
            if (i > 0):
                return False
        return True
            
        