from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        for child in node.children:
            queue.append(child)

# Construct the tree
root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C')]
root.children[0].children = [TreeNode('D'), TreeNode('E')]
root.children[1].children = [TreeNode('F'), TreeNode('G')]

# print(type(root))

# Perform BFS
bfs(root)
