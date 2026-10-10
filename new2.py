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
        values = input("Enter node values: ").split()

        nodes = [None] * n

        i = 0
        while i < n:
            nodes[i] = Node(int(values[i]))
            i = i + 1

        i = 0
        while i < n:
            if 2 * i + 1 < n:
                nodes[i].left = nodes[2 * i + 1]

            if 2 * i + 2 < n:
                nodes[i].right = nodes[2 * i + 2]

            i = i + 1

        self.root = nodes[0]

    def inorder(self):
        stack = [None] * 100
        top = -1
        ptr = self.root

        print("Inorder Traversal:", end=" ")

        while ptr is not None or top != -1:

            while ptr is not None:
                top = top + 1
                stack[top] = ptr
                ptr = ptr.left

            ptr = stack[top]
            top = top - 1

            print(ptr.data, end=" ")

            ptr = ptr.right


tree = BinaryTree()
tree.create_tree()
tree.inorder()