class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node):
    if node is None:
        return
    print(node.value, end=" ")
    for child in node.children:
        dfs(child)

# Construct the tree
root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C')]
root.children[0].children = [TreeNode('D'), TreeNode('E')]
root.children[1].children = [TreeNode('F'), TreeNode('G')]

# Perform DFS
dfs(root)
