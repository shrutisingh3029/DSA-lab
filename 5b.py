class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, x):
    new = Node(x)

    if root == None:
        return new

    temp = root

    while True:
        if x < temp.data:
            if temp.left == None:
                temp.left = new
                break
            temp = temp.left

        else:
            if temp.right == None:
                temp.right = new
                break
            temp = temp.right

    return root


def inorder(root):
    stack = [None] * 100
    top = -1
    temp = root

    while temp != None or top != -1:

        while temp != None:
            top = top + 1
            stack[top] = temp
            temp = temp.left

        temp = stack[top]
        top = top - 1

        print(temp.data, end=" ")
        temp = temp.right


def preorder(root):
    stack = [None] * 100
    top = -1

    if root != None:
        top = top + 1
        stack[top] = root

    while top != -1:
        temp = stack[top]
        top = top - 1

        print(temp.data, end=" ")

        if temp.right != None:
            top = top + 1
            stack[top] = temp.right

        if temp.left != None:
            top = top + 1
            stack[top] = temp.left


root = None

n = int(input("Enter number of students: "))

i = 0
while i < n:
    x = int(input("Enter roll number: "))
    root = insert(root, x)
    i = i + 1

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)