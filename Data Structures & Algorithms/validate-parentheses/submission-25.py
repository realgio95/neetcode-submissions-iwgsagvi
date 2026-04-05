class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        # [ ->] {}()
        # | [ |
        stack = []
        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            if c in closeToOpen.keys():
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
        return True if not stack else False
