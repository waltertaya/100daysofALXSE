# Import the deque class from the collections module. Deque is a double-ended queue which allows
# appending and popping from both ends with O(1) performance.
from collections import deque

# Define the TreeNode class which will represent each node in the tree.
class TreeNode:
    def __init__(self, value):
        self.value = value  # Initialize the node's value.
        self.children = []  # Initialize the node's children as an empty list.

# Define the BFS (Breadth-First Search) function.
def bfs(root):
    if root is None:  # If the root node is None, there's nothing to traverse.
        return
    # Initialize the queue with the root node.
    queue = deque([root])
    while queue:  # Continue looping as long as there are nodes in the queue.
        node = queue.popleft()  # Remove and return the leftmost node from the queue.
        print(node.value, end=" ")  # Print the node's value followed by a space.
        # Add all children of the current node to the queue.
        for child in node.children:
            queue.append(child)

# Construct the tree.
root = TreeNode('A')  # Create the root node with value 'A'.
root.children = [TreeNode('B'), TreeNode('C')]  # Add children 'B' and 'C' to the root.
root.children[0].children = [TreeNode('D'), TreeNode('E')]  # Add children 'D' and 'E' to node 'B'.
root.children[1].children = [TreeNode('F'), TreeNode('G')]  # Add children 'F' and 'G' to node 'C'.

# Optional: Print the type of the root to check the structure.
# print(type(root))

# Perform BFS traversal starting from the root.
bfs(root)
