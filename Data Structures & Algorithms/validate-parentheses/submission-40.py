class Solution:
    def isValid(self, s: str) -> bool:
        cto = {"]":"[", ")":"(", "}":"{"}
        stack = []
        for c in s:
            if c in cto.values():
                stack.append(c)
            elif c in cto.keys():
                if stack and cto[c] == stack[-1]:
                    stack.pop()
                else:
                   return False
        return True if not stack else False


# class Solution:
#     def isValid(self, s: str) -> bool:
#         cto = {"]": "[", ")": "(", "}": "{"}
#         stack = []

#         for c in s:
#             if c in cto.values():  # Check if `c` is an opening bracket
#                 stack.append(c)
#             elif c in cto.keys():  # Check if `c` is a closing bracket
#                 # Check for matching opening bracket or empty stack
#                 if stack and cto[c] == stack[-1]:
#                     stack.pop()  # Remove the matching opening bracket
#                 else:
#                     return False  # Unmatched closing bracket

#         # Stack should be empty if all brackets are matched
#         return not stack