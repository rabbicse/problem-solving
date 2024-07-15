# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        length = len(preorder)
        left = 0
        right = length - 1
        level = 0

        hash_map = {}
        for index, val in enumerate(inorder):
            hash_map[val] = index

        def traverse(left, right):
            nonlocal level
            
            if left > right:
                return

            node_val = preorder[level]
            node = TreeNode(node_val)

            level += 1

            node.left = traverse(left, hash_map[node_val] - 1)
            node.right = traverse(hash_map[node_val] + 1, right)

            return node



        return traverse(left, right)
        
