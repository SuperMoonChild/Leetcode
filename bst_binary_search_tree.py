from typing import Optional, List

#build a treeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    #insert into BST
    def __init__(self):
        self.root = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return TreeNode(val)
        if root.val > val: 
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val: 
            root.right = self.insertIntoBST(root.right, val)
        return root 
    
    #in order traversel of the tree 
    # A utility function to do inorder traversal of BST
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
    
    def preorder(self,root):
        if root:
             print(root.val,end=" ")
             self.preorder(root.left)
             self.preorder(root.right)
    
    def postorder(self,root):
         if root:
             self.postorder(root.left)
             self.postorder(root.right)
             print(root.val,end=" ")

           
    #delete nodes from BST: 
    #helper functions to find the nodes 
    #Find the min node from the righttree 
    def min_node_right(self,root: TreeNode)-> int:
             root = root.right
             while root.left: 
                   root = root.left 
             return root.val
    
    def max_node_left(self,root:TreeNode)->int: 
             root = root.left
             while root.right:
                    root = root.right 
             return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #if root = None, then return the root 
        if not root:
            return None 
        
         #traverse the tree to look for the value: 
        if  key > root.val: 
                 print(root.val)
                 root.right = self.deleteNode(root.right,key)
                 print(root.right)
        elif key < root.val: 
                 print(root.val)
                 root.left = self.deleteNode(root.left,key)
                 print(root.left)
        else: 
             #delete the current node
            if not (root.left or root.right):
                 return None 
            elif root.right: 
                 root.val = self.min_node_right(root)
                 root.right = self.deleteNode(root.right,root.val)
            elif root.left: 
                 root.val = self.max_node_left(root)
                 root.left = self.deleteNode(root.left,root.val)
        return root 
                  
#delete node from the tree 
#There are two cases here: 
#If the node is on the left tree: traverse the rightest child of the tree and replace the 
#node, then delete the original node 
#If the node that is needed to be remove is on the right tree: move to the leftest of the tree 
#and replace, then remove the element 
#sol = Solution()
#new_val = 5
#root = [5,3,6,2,4,,7]
#delete_node = sol.deleteNode(root, new_val)
#print(print_inorder(delete_node))

#print the binary tree
# Driver Code
if __name__ == "__main__":
    tree = BinaryTree()

    # Let us create following BST
    #        50
    #     /     \
    #    30      70
    #   /  \    /  \
    #  20   40  60   80
    tree.root = tree.insertIntoBST(tree.root, 50)
    tree.insertIntoBST(tree.root, 30)
    tree.insertIntoBST(tree.root, 20)
    tree.insertIntoBST(tree.root, 40)
    tree.insertIntoBST(tree.root, 70)
    tree.insertIntoBST(tree.root, 60)
    tree.insertIntoBST(tree.root, 80)

    """
    Original BST: 20 30 40 50 60 70 80 
    preorder Traversal of BST 50 30 20 40 70 60 80 
    postoder Traversal of BST 20 40 30 60 80 70 50 
    """

    print("Original BST:", end=" ")
    #print the original tree through BST 
    tree.inorder(tree.root)
    print()

    print("preorder Traversal of BST",end=" ")
    tree.preorder(tree.root)
    print() 

    print("postoder Traversal of BST",end=" ")
    tree.postorder(tree.root)
    print()

    print("\nDelete a Leaf Node: 20")
    tree.root = tree.deleteNode(tree.root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with single child: 70")
    tree.root = tree.deleteNode(tree.root, 70)
    print("Modified BST tree after deleting single child Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with both child: 50")
    tree.root = tree.deleteNode(tree.root, 50)
    print("Modified BST tree after deleting both child Node:")
    tree.inorder(tree.root)


"""Let's do some of dry run on the code: 
root val = 50 
remove val = 20 
going in the loop: 
root.right = self.deleteNode(root.right,key)
root val = 30 
20 < 30, going to the left 
We found the node = 20, need to delete 20 node 
if not (root.left or root.right):
then we return None for removing the 20 of the node 
"""

"""
Let's dry run if we need to remove a node with two children 
remove 70 from the list 
the val > root.val, the go to right 
then we find the node = 70 and they have two children
then we need to find the leftest value of the tree 
then we find 60, then put the root.val = 60 
Then, we are going to remove 60 at the end node 
 if not (root.left or root.right):
                 return None
then we return None instead of the None = null 
"""
#three types of search inorder,preorder and post order search 


#Depth First Search 
"""
Inorder Traversal: O(n), you have to go through every single node 
Insertion (n*logn) building an entire tree 
The total time  O(nlog) + O(n), therefore we have O(nlogn)

All the above of the three traversal is DFS 
We went to the botton of the tree 
"""

#BFS 
"""
In depth-first search, we prioritized depth. For breath-first serach, we prioritize breadth. We focus visiting all the nodes on one level before moving on to the next level.
Generally, breadth-first search is implemented iteratively and that is the implementation we will be covering in this course. You can write it recursively but it is a lot more challenging.
BFS makes use of a queue data structure, more specifically, a deque, allowing us to remove elements both from the head and the tail in 𝑂(1)and O(1) time. This will make sense soon.

*Why use queue to do BFS traversal: 
The queue supports FIFO behavior, which is essential for BFS. In BFS, 
you explore all nodes at the present depth level before you move on to nodes at the next depth level. This ensures that nodes are explored in the order they are discovered.

For a Tree, we go through layers by layers and print from left to right (common practice)

Technically, the total work done is c∗n where n is the number of nodes in the tree and 
c is the amount of work we perform at each node. We performed a total of three operations per node - printing the node, appending the node, and removing it. This is what the 
c represents. For the case of asymptotic analysis, we can drop this constant, meaning the algorithm belongs to 
𝑂(𝑛)
"""

#Here is an example of how I use the deque 
from collections import deque

d = deque([1, 2, 3, 4, 5])
d.append(6)  # deque becomes [1, 2, 3, 4, 5, 6]
d.appendleft(0)  # deque becomes [0, 1, 2, 3, 4, 5, 6]
print(d.pop())  # returns 6, deque becomes [0, 1, 2, 3, 4, 5]
print(d.popleft())  # returns 0, deque becomes [1, 2, 3, 4, 5]
d.extend([7, 8])  # deque becomes [1, 2, 3, 4, 5, 7, 8]
d.extendleft([10, 20])  # deque becomes [20, 10, 1, 2, 3, 4, 5, 7, 8]
d.rotate(3)  # rotates right by 3 places
print(d)  # outputs deque([4, 5, 7, 8, 20, 10, 1, 2, 3])

#build a simple tree for test 
root_2 = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7)))

#breadth search traversal 
from collections import deque
def bfs(root):
    
    queue=deque() 

    if root: 
         queue.append(root)
    
    level = 0 
    
    while len(queue) > 0: 

        for i in range(len(queue)): 
             #pop the first value 
             print("level: ", level)
             curr = queue.popleft() 
             
             if curr.left:
                  queue.append(curr.left)
             if curr.right: 
                  queue.append(curr.right)
        level+=1  
     
bfs(root_2)  

####From LeetCode questions####
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        que = deque([root])

        while que:
            size = len(que)
            level = []
            for i in range(size):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(level)

        return result

"""
Let's dry run some of the example: root = [3,9,20,null,null,15,7] 
beginning to traverse with root: deque([root])
size = 3 
loop through the size 
node = popleft so node = 3 
level.append(3) 
return level = 3 
result = [[3]]
traverse through the tree: left = 9, right = 20 

"""
