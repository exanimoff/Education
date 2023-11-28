class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def find(root, target) -> bool:
    if root is None:
        return False

    if root.value == target:
        return True

    for child in root.children:
        if find(child, target):
            return True

    return False

root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(55)]
root.children[1].children[0].children = [TreeNode(60)]

target = 60
found = find(root, target)

if found:
    print(f"Значение {target} найдено в дереве.")
else:
    print(f"Значение {target} не найдено в дереве.")

