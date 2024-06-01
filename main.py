class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_min_root(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def find_max_root(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

def find_sum_root(root):
    if root is None:
        return 0
    return root.val + find_sum_root(root.left) + find_sum_root(root.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


min_value = find_min_root(root)
max_value = find_max_root(root)
sum_max = find_sum_root(root)
print(f"у двійковому дереві знайдено найменше значення {min_value}")
print(f"У двійковому дереві знайдено найбільше значення {max_value}")
print(f"Сума всіх значень у двійковому дереві {sum_max}")