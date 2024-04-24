class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root, depth=0):
    if not root:
        print(f"{'  ' * depth}到达空节点，返回高度 -1")
        return 0  # 如果树为空，返回 -1
    else:
        print(f"{'  ' * depth}访问节点 {root.val}")
        left_height = height(root.left, depth + 1)
        right_height = height(root.right, depth + 1)
        current_height = 1 + max(left_height, right_height)
        print(f"{'  ' * depth}节点 {root.val} 的左子树高度为 {left_height}, 右子树高度为 {right_height}, 当前高度为 {current_height}")
        return current_height

# 示例构建一个简单的树
#树 
"""
      1 
    2   3 
  4  5     6 
"""

"""
中间值：print 
访问节点 1
  访问节点 2
    访问节点 4
      到达空节点，返回高度 -1
      到达空节点，返回高度 -1
    节点 4 的左子树高度为 -1, 右子树高度为 -1, 当前高度为 0
    访问节点 5
      到达空节点，返回高度 -1
      到达空节点，返回高度 -1
    节点 5 的左子树高度为 -1, 右子树高度为 -1, 当前高度为 0
  节点 2 的左子树高度为 0, 右子树高度为 0, 当前高度为 1
  访问节点 3
    到达空节点，返回高度 -1
    访问节点 6
      到达空节点，返回高度 -1
      到达空节点，返回高度 -1
    节点 6 的左子树高度为 -1, 右子树高度为 -1, 当前高度为 0
  节点 3 的左子树高度为 -1, 右子树高度为 0, 当前高度为 1
节点 1 的左子树高度为 1, 右子树高度为 1, 当前高度为 2
二叉树的总高度是: 2
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# 调用函数
##tree_height = height(root)
#print("二叉树的总高度是:", tree_height)

def min_depth(root): 
    if not root:
        return 0 
    
    if not root.left:
        return 1+min_depth(root.right)
    elif not root.right:
        return 1+min_depth(root.left)
    else:
        return 1+ min(min_depth(root.right),min_depth(root.left))
    
from typing import Optional
class Solution:
    def identicalTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True  # Both trees are empty, hence identical
        if not tree1 or not tree2:
            return False  # One tree is empty, the other is not
        return (
            tree1.val == tree2.val and
            self.identicalTree(tree1.left, tree2.left) and
            self.identicalTree(tree1.right, tree2.right)
        )
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True  # An empty subtree is always a subtree of any tree
        if not root:
            return False  # Non-empty subtree cannot be found in an empty tree
        if self.identicalTree(root, subRoot):
            return True  # Check if the current trees are identical
        # Recursively check subtrees of the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# TreeNode class definition remains the same as provided before

# Create the main tree
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Create the subtree
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Create an instance of Solution and test the isSubtree function
solution = Solution()
result = solution.isSubtree(root, subRoot)
print("Is subRoot a subtree of root?", result)
