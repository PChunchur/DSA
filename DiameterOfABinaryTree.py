# to Calculate the diameter of a binarry tree
# Given a tree compute the length of the longest path between any two nodes in a tree

# *LOGIC*
# The diameter of a tree T is the largest of the following quantities:
# 1. The diameter of T's left subtree
# 2. The diameter of T's right subtree
# 3. The longest path between leaves that goes through the root of T


class TreeNode:
    def __init_(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = [0]
        
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            result[0] = max(res[0], left + right + 2)
            
            return 1 + max(left,right)
        
        dfs(root)
        
        return result[0]