class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not node:
        return []

    queue = [node]
    index = 0
    while index <= len(queue) - 1:
        node = queue[index]
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        index += 1

    return [x.value for x in queue]


if __name__ == '__main__':
    root = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
    print(tree_by_levels(root))
