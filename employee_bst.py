class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    new = Node(data)

    if root == None:
        return new

    temp = root

    while True:
        if data < temp.data:
            if temp.left == None:
                temp.left = new
                break
            else:
                temp = temp.left

        else:
            if temp.right == None:
                temp.right = new
                break
            else:
                temp = temp.right

    return root


def level_order(root):
    if root == None:
        return

    queue = [None] * 100
    front = 0
    rear = 0

    queue[rear] = root
    rear = rear + 1

    while front < rear:
        temp = queue[front]
        front = front + 1

        print(temp.data, end=" ")

        if temp.left != None:
            queue[rear] = temp.left
            rear = rear + 1

        if temp.right != None:
            queue[rear] = temp.right
            rear = rear + 1

    print()


def height(root):
    if root == None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


def print_leaf(root):
    if root == None:
        return

    if root.left == None and root.right == None:
        print(root.data, end=" ")

    print_leaf(root.left)
    print_leaf(root.right)


# Main program

root = None
new_root = None

n = int(input("Enter number of employees: "))

i = 0
while i < n:
    x = int(input("Enter employee ID: "))

    root = insert(root, x)
    new_root = insert(new_root, x)

    i = i + 1


print("\nOriginal BST Level Wise:")
level_order(root)

print("\nNew BST Level Wise:")
level_order(new_root)

print("\nHeight of BST:", height(root))

print("Leaf Nodes: ", end="")
print_leaf(root)
print()