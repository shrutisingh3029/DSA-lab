class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        n = int(input("Enter number of nodes: "))
        values = list(map(int, input("Enter node values: ").split()))

        nodes = [Node(x) for x in values]

        for i in range(n):
            if 2 * i + 1 < n:
                nodes[i].left = nodes[2 * i + 1]

            if 2 * i + 2 < n:
                nodes[i].right = nodes[2 * i + 2]

        self.root = nodes[0]

    def inorder(self):
        stack = []
        ptr = self.root

        print("Inorder Traversal:", end=" ")

        while ptr is not None or stack:
            while ptr is not None:
                stack.append(ptr)
                ptr = ptr.left

            ptr = stack.pop()
            print(ptr.data, end=" ")

            ptr = ptr.right


tree = BinaryTree()
tree.create_tree()
tree.inorder()