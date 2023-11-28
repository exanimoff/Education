class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    def dfs(node):
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        nonlocal max_diameter
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    max_diameter = 0
    dfs(root)
    return max_diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)


result = diameter_of_binary_tree(root)
print("Диаметр дерева:", result)
