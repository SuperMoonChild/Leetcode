#build a new tree 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#build a new Tree 
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(root)
# 构建一个简单的树:   5
#                    / \
#                   4   8
#                  /   / \
#                 11  13  4
#                /  \      \
#               7    2      1

#find a path that does not contain zero 
def canReachLeaf(root,path):

    if not root or root.val == 0: 
        return False 
    
    path.append(root.val)
    
    if canReachLeaf(root.left,path):
        return True 
    elif canReachLeaf(root.right,path):
        return True 
    elif not root.left or not root.right: 
        return True
    path.pop() 
    return False 

path = []
#print(canReachLeaf(root,path))

# 构建一个简单的树:      5
#                    / \
#                   4   8
#                  /   / \
#                 11  13  4
#                /  \      \
#               7    2      1

#write a function to find the target sum variable 
"""
1.设计思路
2.DFS Traversal of the Tree 
3. Design end case: Traverse to null root 
4. Design end case: The targetsum = leaf node 
5. recursive function 
"""
def hastargetSum(root,targetSum):
    #terminate condition, basecase 
    if not root:
        print(f"到达空节点，返回False")
        return False 
    
    print(f"访问节点 {root.val}，当前路径需和为 {targetSum - root.val}")
    
    #Output Condition 
    if (not root.left and not root.right):
        if root.val == targetSum:
            print(f"叶子节点 {root.val}，路径和 {targetSum - root.val}正确，返回True")
            return True 
    
    right = hastargetSum(root.right,targetSum - root.val)
    left = hastargetSum(root.left,targetSum-root.val)

    return left or right 

targetSum = 26
print(hastargetSum(root,targetSum))
