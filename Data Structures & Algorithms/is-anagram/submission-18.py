class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = [0] * 26

        for n in s:
            cnt_s[ord(n)-ord('a')] += 1 
        for v in t:
            cnt_s[ord(v)-ord('a')] -= 1

        # go through cnts make sure all is 0 aka nothing not equal 0 then return true
        for j in cnt_s:
            if j != 0:
                return False

        return True   