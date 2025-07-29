def find_kth_largest(root, k):
    # Use reverse in-order traversal (right-root-left)
    def reverse_inorder(node):
        nonlocal k, result
        if node and node.value is not None:
            reverse_inorder(node.right)
            if k == 0:
                return
            k -= 1
            if k == 0:
                result = node.value
                return
            reverse_inorder(node.left)

    result = None
    reverse_inorder(root)
    return result