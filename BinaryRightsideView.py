#Right side view of a binary tree 

#Logic:
# 1. Initialise empty queue, enqueue the root of the tree 
# 2. While queue is not empty, get the sizze of the current level, 
#     then traverse the nodes at the current leve;
# 3. Dequeue the node, if it is the last node of the current level, 
#     then add it to the result
# 4. If the node has left child, then add it to the queue
# 5. If the node has right child, then add it to the queue
# 6. Return the result

from collections import deque

class Node:
    def __init__(self, data):                               #initialise the node
        self.data = data                                    #data of the node
        self.left = None
        self.right = None
        
class Solution:                                             #class solution
    def rightView(self,root):                               #function rightView
        if not root:                                        #if root is empty, then return empty
            return[]
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range (n):
                current = queue.popleft()
                if i == n-1:
                    result.append(current.data)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
               
        return result
    
    def buildTree(s):                                         #function buildTree
        if not s or s[0] == 'null':                          #if s is empty or s[0] is null, then return None
            return None
    
        ip = s.split()
        root = Node(int(ip[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(ip):
            currentNode - queue.popleft()
            
            currentVal = ip[i]
            if currentVal != 'null':
                currentNode.left = Node(int(currentVal))
                queue.append(currentNode.left)
                i += 1
                
                if i >= len(ip):
                    break
                
            currentVal = ip[i]
            if currentVal != 'null':
                currentNode.right = Node(int(currentVal))
                queue.append(currentNode.right)
                i += 1
        return root
    
    if __name__ == '__main__':
        t = int(input(strip()))
        for _ in range(t):
            s = input().strip()
            root = buildTree(s)
            solution = Solution()
            arr = solution.rightView(root)
            for x in arr:
                print(x, end = '')
            print()

