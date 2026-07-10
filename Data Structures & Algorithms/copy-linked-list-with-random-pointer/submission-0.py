"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None:None }
        
        oldNode = head
        while oldNode:
            copy = Node(oldNode.val)
            oldToCopy[oldNode] = copy
            oldNode = oldNode.next

        oldNode = head
        while oldNode:
            copy = oldToCopy[oldNode] 
            copy.next = oldToCopy[oldNode.next]
            copy.random = oldToCopy[oldNode.random]
            oldNode = oldNode.next

        return oldToCopy[head]
