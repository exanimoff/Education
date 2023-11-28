class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            # Left Right Case
            if key > root.left.key:
                root.left = self.rotate_left(root.left)
            # Left Left Case
            return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            # Right Left Case
            if key < root.right.key:
                root.right = self.rotate_right(root.right)
            # Right Right Case
            return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            # Left Right Case
            if self.balance_factor(root.left) < 0:
                root.left = self.rotate_left(root.left)
            # Left Left Case
            return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            # Right Left Case
            if self.balance_factor(root.right) > 0:
                root.right = self.rotate_right(root.right)
            # Right Right Case
            return self.rotate_left(root)

        return root

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def display(self):
        print("Inorder traversal of the AVL tree:")
        result = self.inorder_traversal(self.root)
        print(result)


# Пример использования:
avl_tree = AVLTree()
avl_tree.insert_key(10)
avl_tree.insert_key(20)
avl_tree.insert_key(30)

avl_tree.display()

avl_tree.delete_key(20)

avl_tree.display()
