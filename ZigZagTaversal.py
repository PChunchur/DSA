#Zig zag order traversal of a binary tree


from collections import deque

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right
        
class Solution:
    def ZigZag(self, root: optional[TreeNode] ) -> List[List[int]]:
        result = []
        queue = deque([root] if root else [])
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popeft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level = reversed(level) if len(result) % 2 else level    
            result.append(level)
            
        return result
    
# Initial State:

'''
* LOGIC *

res = []                     res is initialized as an empty list to store the final result
queue = deque([1])           is initialized as a deque (double-ended queue) containing the root node if the root is not None. 
                             If the root is None, queue is initialized as an empty deque.

                             The while loop runs as long as there are nodes in the queue.
                             level is initialized as an empty list to store the values of nodes at the current level.

Level 1:

level = []
Dequeue 1, append its value to level → level = [1]
Enqueue 2 and 3 → queue = deque([2, 3])
Since the level number is 0 (even), append level to res → res = [[1]]
Level 2:

level = []
Dequeue 2, append its value to level → level = [2]
Enqueue 4 and 5 → queue = deque([3, 4, 5])
Dequeue 3, append its value to level → level = [2, 3]
Enqueue 6 → queue = deque([4, 5, 6])
Since the level number is 1 (odd), reverse level and append it to res → res = [[1], [3, 2]]
Level 3:

level = []
Dequeue 4, append its value to level → level = [4]
Dequeue 5, append its value to level → level = [4, 5]
Dequeue 6, append its value to level → level = [4, 5, 6]
Since the level number is 2 (even), append level to res → res = [[1], [3, 2], [4, 5, 6]]'''