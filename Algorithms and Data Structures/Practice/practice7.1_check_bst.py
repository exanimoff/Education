class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_binary_search_tree(root):
    def check_nodes(node, min_value, max_value):
        if node is None:
            return True

        if min_value is not None and node.value <= min_value:
            return False

        if max_value is not None and node.value >= max_value:
            return False

        left = check_nodes(node.left, min_value, node.value)
        right = check_nodes(node.right, node.value, max_value)

        return left and right

    return check_nodes(root, None, None)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = is_binary_search_tree(root)
print(result)

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)

result = is_binary_search_tree(root)
print(result)
