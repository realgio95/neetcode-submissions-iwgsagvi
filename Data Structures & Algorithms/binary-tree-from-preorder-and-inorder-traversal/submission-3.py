# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #  understand, plan, execute, review

        # preorder - 1 2 3 4
        # inorder 2 1 3 4
        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])
        # inorder.indexof(root) - note ==> find python equivalent
        p = -1 # root index in inorder list
        i = 0
        for i in range(0, len(inorder)): 
            if root.val == inorder[i]:
                p = i
        
        # 1
        # left - buildTree 2
        #     root 2
        # right  buildTree 3 4
        #     root 3
        #         left none
        #         right buildTree 4

        preorderLen = len(preorder)
        root.left = self.buildTree(preorder[1:p+1],inorder[0:p])
                                    #  pr 1:2 [2], or: 0:1 - [2] 
        root.right = self.buildTree(preorder[p+1:preorderLen],inorder[p+1:preorderLen])
                                    #  pr 2:4 [3, 4], or: 2:4 [3,4] 
        return root

        